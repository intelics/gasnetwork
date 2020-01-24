"""
    File for converting engineering units
"""

UNITS_LOOKUP = {}
UNITS_LOOKUP['pressure'] = []
UNITS_LOOKUP['pressure'].append({'units': 'Pa', 'gain': 1, 'bias': 0})
UNITS_LOOKUP['pressure'].append({'units': 'kPag', 'gain': 0.001, 'bias': -101325})
UNITS_LOOKUP['svf'] = []
UNITS_LOOKUP['svf'].append({'units': 'Sm3/s', 'gain': 4237819.2, 'bias': 0})
UNITS_LOOKUP['svf'].append({'units': 'MMSCFD', 'gain': 3.058175869, 'bias': 0})

def convert_value(measurement, value, units):
    ret_val = value
    if measurement in UNITS_LOOKUP:
        for conversion in UNITS_LOOKUP[measurement]:
            if conversion['units'] == units:
                ret_val = (value - conversion['bias']) * conversion['gain']
    return ret_val
