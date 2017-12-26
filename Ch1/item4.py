#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER1
"""

from urllib.parse import parse_qs
from functions import get_first__int

COLORS = parse_qs('red=5&green=&blue=0', keep_blank_values=True)

print(COLORS)

print('Red     :', COLORS.get('red'))
print('Green   :', COLORS.get('green'))
print('Opacity :', COLORS.get('opacity'))

print('Red     :', get_first__int(COLORS, 'red'))
print('Green   :', get_first__int(COLORS, 'green'))
print('Opacity :', get_first__int(COLORS, 'opacity'))
