from functools import reduce
import pandas as pd
import numpy as np
from hestia_earth.schema import TermTermType
from hestia_earth.utils.model import find_primary_product
from hestia_earth.utils.tools import list_sum, list_average, flatten
from hestia_earth.utils.api import download_hestia

INDEX_COLUMN = 'cycle.id'
YIELD_COLUMN = 'Grain yield (kg/ha)'
FERTILISER_COLUMNS = [
    'Nitrogen (kg N)',
    'Phosphorus (kg P2O5)',
    'Potassium (kg K2O)',
    'Magnesium (kg Mg)'
    # 'Sulphur (kg S)'
]
FERTILISER_TERM_TYPES = [
    TermTermType.ORGANICFERTILISER.value,
    TermTermType.INORGANICFERTILISER.value
]
PESTICIDE_COLUMN = 'pesticideUnspecifiedAi'  # 'Total pesticides (kg active ingredient)'
IRRIGATION_COLUMN = 'waterSourceUnspecified'  # 'Total water inputs (m3 / ha)'


def _nansum(val1: float, val2: float):
    return np.nan if all([np.isnan(val1), np.isnan(val2)]) else np.nansum([val1, val2])


def get_input_group(input: dict):
    term_units = input.get('term', {}).get('units')
    return next((group for group in FERTILISER_COLUMNS if term_units in group), None)


def _group_inputs(inputs: list):
    def exec(group: dict, group_key: str):
        sum_inputs = list_sum(flatten([
            input.get('value', []) for input in inputs if get_input_group(input) == group_key
        ]), np.nan)
        return {**group, group_key: sum_inputs}
    return exec


def _sum_input_values(inputs: list, percentages: list = []):
    vals = flatten([input.get('value', []) for input in inputs])
    return list_sum(vals, np.nan) if not percentages else np.dot(vals, percentages)


def _pct_activate_ingredients(brand_name: str):
    name = download_hestia(brand_name, 'Term')
    return list_sum([i.get('value') for i in name.get('defaultProperties', [])
                     if i.get('term', {}).get('@id') == 'activeIngredient'], np.nan)


def _pesticideBrandNames_per_cycle(cycle: dict):
    return [
            i for i in cycle.get('inputs', []) if all([
                i.get('term', {}).get('termType') == TermTermType.PESTICIDEBRANDNAME.value,
                list_sum(i.get('value', []), np.nan) >= 0  # default nan, instead of zero 0
            ])
    ]


def _pesticideBrandName_IDs_per_cycle(cycle: dict):
    brandnames = _pesticideBrandNames_per_cycle(cycle)
    return [i.get('term', {}).get('@id') for i in brandnames]


def _get_totalAI_of_brandnames(cycles: list):
    pestBrandNames = list(set(flatten([_pesticideBrandName_IDs_per_cycle(c) for c in cycles])))
    pct_ai = [_pct_activate_ingredients(brand) for brand in pestBrandNames]
    return {pestBrandNames[i]: pct_ai[i] for i in range(len(pestBrandNames))}


def group_cycle_inputs(cycle: dict, brandname_to_ai: dict = {}):
    brandname_to_ai = brandname_to_ai or _get_totalAI_of_brandnames([cycle])

    fertilisers = [
        i for i in cycle.get('inputs', []) if all([
            i.get('term', {}).get('termType') in FERTILISER_TERM_TYPES,
            list_sum(i.get('value', []), np.nan) >= 0
        ])
    ]
    fertilisers_values = reduce(_group_inputs(fertilisers), FERTILISER_COLUMNS, {})

    pestAIs = [
        i for i in cycle.get('inputs', []) if all([
            i.get('term', {}).get('termType') == TermTermType.PESTICIDEAI.value,
            list_sum(i.get('value', []), np.nan) >= 0
        ])
    ]
    pestBrandNames = _pesticideBrandNames_per_cycle(cycle)
    pestAI_percentages = [brandname_to_ai.get(brand_name.get('term', {}).get('@id')) for brand_name in pestBrandNames]

    return {
        INDEX_COLUMN: cycle.get('@id'),
        YIELD_COLUMN: list_average((find_primary_product(cycle) or {}).get('value', []), np.nan),
        **fertilisers_values,
        'completeness.fertiliser': cycle.get('completeness', {}).get('fertiliser', False),
        PESTICIDE_COLUMN: _nansum(_sum_input_values(pestAIs), _sum_input_values(pestBrandNames, pestAI_percentages)),
        'completeness.pesticidesAntibiotics': cycle.get('completeness', {}).get('pesticidesAntibiotics', False)
    }


def cycle_yield_distribution(cycles: list):
    dict_brandname_to_ai = _get_totalAI_of_brandnames(cycles)

    values = list(map(lambda c: group_cycle_inputs(c, dict_brandname_to_ai), cycles))
    # in case there are no values, we should still set the columns
    columns = group_cycle_inputs({}).keys()
    return pd.DataFrame.from_records(values, index=[INDEX_COLUMN], columns=columns)
