#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Functions for scripts in chapter1.
"""

def get_first__int(values, key, default=0):
    """
    Return the value hit by the given key at first.
    If the key is not found, return default value.
    """
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found
