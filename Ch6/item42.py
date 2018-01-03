#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER6
"""


from functools import wraps

def trace(func):
    """
    Trace execution of the function
    """
    @wraps(func)
    def _wrapper(*args, **kwards):
        ret = func(*args, **kwards)
        print('%s(%r, %r) -> %r' % (func.__name__, args, kwards, ret))
        return ret
    return _wrapper

@trace
def fibonacci(n):
    """
    Return the n-th Fibonacci number
    """
    if n in (0, 1):
        return n
    return fibonacci(n-2) + fibonacci(n-1)

fibonacci(3)
help(fibonacci)
