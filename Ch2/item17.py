#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER2
"""

def __normalize(numbers):
    total = sum(numbers)
    return [x / total for x in numbers]

def __normalize_defesive(numbers):
    if iter(numbers) is iter(numbers):
        raise TypeError('Must supply a container')
    return __normalize(numbers)

class _ReadVisits(object):
    def __init__(self, data_path):
        self.__data_path = data_path
    def __iter__(self):
        with open(self.__data_path) as file:
            for line in file:
                yield int(line)

VISITS_CONTAINER = _ReadVisits('visits.txt')
PERCENTAGE_VISITS = __normalize(VISITS_CONTAINER)
print(PERCENTAGE_VISITS)

VISITS = [15, 35, 80]
print(__normalize_defesive((VISITS)))
print(__normalize_defesive(iter(VISITS)))
