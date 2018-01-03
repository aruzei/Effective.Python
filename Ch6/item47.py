#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER6
"""

from decimal import Decimal

def _print_cost(rate, seconds):
    cost = rate * seconds / 60
    print(cost)
    print(round(cost, 2))
    print(Decimal(cost).quantize(Decimal('0.001')))

_print_cost(1.45, 3 *60 + 42)
_print_cost(0.05, 5)
_print_cost(Decimal(0.05), Decimal(5))
