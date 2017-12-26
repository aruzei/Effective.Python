#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER1
"""

ZERO_NINE = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
EVENS = ZERO_NINE[::2]
ODDS = ZERO_NINE[1::2]
print(EVENS)
print(ODDS)

PYTHON = 'パイソン'
BINARY_PYTHON = PYTHON.encode('utf-8')
INVALID_BINARY_NOHTYP = BINARY_PYTHON[::-1]

print(PYTHON)
print(BINARY_PYTHON)
print(INVALID_BINARY_NOHTYP)

# We can't decode this.
# INVALID_NOHTYP = INVALID_BINARY_NOHTYP.decode('utf-8')
# print(INVALID_NOHTYP)
