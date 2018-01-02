#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER5
"""

from threading import Thread
from Profiles import profile_func

def _factorize(number):
    print(number)
    for i in range(1, number + 1):
        if number % i == 0:
            yield i

NUMBERS = [123456, 123456, 123456, 123456]
def _run_factorize():
    for number in NUMBERS:
        list(_factorize(number))

class _FactorizeThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number
        self.factors = []

    def run(self):
        self.factors = list(_factorize(self.number))

def _run_factorize_threads():
    for number in NUMBERS:    
        thread = _FactorizeThread(number)
        thread.start()
        thread.join()

profile_func(_run_factorize)
profile_func(_run_factorize_threads)
