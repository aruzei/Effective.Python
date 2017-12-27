#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER2
"""


def __log(message, values):
    if not values:
        print(message)
    else:
        value_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, value_str))


def __log2(message, *values):
    """
    Log message and values.
    Values are always tranlated to tuple. So this method may consume memory.
    """
    __log(message, values)

__log("My numbers are", [1, 2])
__log("Hello World.", [])
__log2("Hello World.")
