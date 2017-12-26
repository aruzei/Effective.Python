#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER1
"""

ZERO_NINE = list(range(0, 10, 1))

ITERATIVE_EVENS = (x for x in ZERO_NINE if x % 2 == 0)
ITERATIVE_ENVEN_SQUARES = (x ** 2 for x in ITERATIVE_EVENS)
ENVEN_SQUARES_OVER20 = [x for x in ITERATIVE_ENVEN_SQUARES if x > 20]

print(ENVEN_SQUARES_OVER20)
