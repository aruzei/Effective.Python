#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER8
"""

from profiles import profile_func
from time import sleep

def gcd(pair):
    def _():
        m, n = pair
        low = min(m, n)
        for i in range(low, 0, -1):
            if m % i == 0 and n % i == 0:
                print(i)
                return i
    return _

GCD = gcd((123451234512345, 5554545))

profile_func(GCD)
