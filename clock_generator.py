#!/usr/bin/env python3

import re
import serial

integer_re = re.compile(r"[0-9]+")
units_re   = re.compile(r"([MmKk])\s*[Hh]z")

freq_str = input('Clock frequency: ')
freq_m = integer_re.match(freq_str)
units_m = units_re.search(freq_str)

freq = 0
units = 1

if freq_m is None:
    print('Unrecognized clock frequency')
else:
    freq = int(freq_m.group())

if units_m is not None:
    match units_m.group(1):
        case 'M':
            units = 1000000
        case 'm':
            units = 1000000
        case 'K': 
            units = 1000
        case 'k':
            units = 1000
        case default:
            units = 1

freq = freq * units

print('Setting frequency: ' + str(freq))