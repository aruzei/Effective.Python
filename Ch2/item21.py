#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER2
"""


def __safe_division(dividend, divisor, *,
                    ignore_overflow=False,
                    ignore_zero_divition=False):
    try:
        return dividend / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_divition:
            return float('inf')
        else:
            raise

print(__safe_division(1.0, 10 ** 500, ignore_overflow=True, ignore_zero_divition=False))
print(__safe_division(1.0, 0, ignore_zero_divition=True))
print(__safe_division(1.0, 10 ** 500, ignore_overflow=True))
print(__safe_division(1.0, 10 ** 500, ignore_overflow=False, ignore_zero_divition=False))
