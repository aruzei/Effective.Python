#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER1
"""

NAMES = ['Cecilla', 'Lise', 'Marie']

def get_longest_name1(names):
    """
    Return the longest name in names
    """

    letters = [len(n) for n in names]
    longest_name = None
    max_letters = 0

    for i, name in enumerate(names):
        count = letters[i]
        if max_letters < count:
            longest_name = names[i]
            max_letters = count
    return longest_name

def get_longest_name2(names):
    """
    Return the longest name in names
    """

    letters = [len(n) for n in names]
    longest_name = None
    max_letters = 0

    for name, count in zip(names, letters):
        if max_letters < count:
            longest_name = name
            max_letters = count
    return longest_name

print(get_longest_name1(NAMES))
print(get_longest_name2(NAMES))
