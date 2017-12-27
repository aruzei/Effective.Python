#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER2
"""


def __sort(comparables, group):
    found = False
    def __closure(value):
        nonlocal found
        if value in group:
            found = True
            return (0, value)
        return(1, value)
    comparables.sort(key=__closure)
    return found


class _Sorter(object):
    def __init__(self, group):
        self.__group = group
        self.found = False
    def __call__(self, value):
        if value in self.__group:
            self.found = True
            return (0, value)
        return(1, value)

NUMBERS = [8, 3, 1, 2, 5, 4, 7, 6]
GROUP1 = {2, 3, 5, 7}
GROUP2 = {0}

print(NUMBERS)
print()

print(__sort(NUMBERS, GROUP2))
print(NUMBERS)

MY_SORTER = _Sorter(GROUP1)
NUMBERS.sort(key=MY_SORTER)
print(MY_SORTER.found)
print(NUMBERS)
