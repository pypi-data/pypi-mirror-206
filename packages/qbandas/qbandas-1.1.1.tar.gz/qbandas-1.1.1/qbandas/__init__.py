"""
Integrates the popular data handling library Pandas and the QuickBase 
API.
"""

__all__ = [ 
    'headers',
    'schema',
    'records',
    'util',
    ]

# from ... import (
#     fetch_records,
#     send_records,
    
#     list_tables,
#     cache_table,
#     
    
#     list_profiles,
#     create_profile,
#     <> remove_profile,
    
#     <> configure_table,
#     <> configure_profile,    
# )

# scoped setup function to avoid cluttering package 
def setup1():
    '''
    Create field types dict by reading in ./data/field_types.json and 
    resolving the packing functions
    '''

    import json
    from os.path import dirname, join, realpath

    from .pack import PACKING_FUNCS

    # field_types is the raw json to dict
    here = dirname(realpath(__file__))
    with open(join(here, 'data', 'field_types.json')) as f:
        field_types = json.load(f)

    # resolve the packing functions
    for t in field_types:
        if field_types[t]["pack"]:
            field_types[t]["pack"] = PACKING_FUNCS[field_types[t]["pack"]]
    
    return field_types
FIELD_TYPES = setup1()

from . import headers, records, schema, util
