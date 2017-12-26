#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER1
"""

ZERO_NINE = list(range(0, 10, 1))
SQUARES = [x*x for x in ZERO_NINE]
SQUARES_MAPPED = map(lambda x: x**2, ZERO_NINE)

print(SQUARES)
print(SQUARES_MAPPED)

EVEN_SQUARES = [x*x for x in ZERO_NINE if x % 2 == 0]
print(EVEN_SQUARES)

CHILE_RANKS = {'ghost':1, 'habanero': 2, 'cayenne': 3}

RANK_DICT = {rank : name for name, rank in CHILE_RANKS.items()}
CHILE_LEN_SET = {len(name) for name in RANK_DICT.values()}

print(RANK_DICT)
print(CHILE_LEN_SET)
