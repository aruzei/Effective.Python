#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER5
"""

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
from Profiles import profile_func

def gcd(pair):
    m, n = pair
    low = min(m, n)
    for i in range(low, 0, -1):
        if m % i == 0 and n % i == 0:
            return i

class Pool(object):
    def map(self, func, numbers):
        return map(func, numbers)

NUMBERS = [(19633109, 2122653), (19633109, 2122653), (19633109, 2122653), (19633109, 2122653)]
MAX_WORKERS = 4
def run(pool, func, numbers):
    print(list(pool.map(func, numbers)))

def main():
    """
    Main method
    """
    def _run1():
        pool = Pool()
        run(pool, gcd, NUMBERS)
    def _run2():
        pool = ThreadPoolExecutor(max_workers=MAX_WORKERS)
        run(pool, gcd, NUMBERS)
    def _run3():
        pool = ProcessPoolExecutor(max_workers=MAX_WORKERS)
        run(pool, gcd, NUMBERS)

    profile_func(_run1)
    profile_func(_run2)
    profile_func(_run3)

# to avoid runtime error in windows
if __name__ == '__main__':
    main()
