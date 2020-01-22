"""
    File for converting engineering units
"""

UNITS_LOOKUP = {}
UNITS_LOOKUP['pressure'] = []
UNITS_LOOKUP['pressure'].append({'units': 'Pa', 'gain': 1, 'bias': 0})
UNITS_LOOKUP['pressure'].append({'units': 'kPag', 'gain': 0.001, 'bias': -101325})

def convert_value(measurement, value, units):
    # convert pressure in given units
    ret_val = value
    if measurement in UNITS_LOOKUP:
        for conversion in UNITS_LOOKUP[measurement]:
            if conversion['units'] == units:
                ret_val = (value - conversion['bias']) * conversion['gain']
    return ret_val
