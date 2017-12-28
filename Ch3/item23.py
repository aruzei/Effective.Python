#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER3
"""
from collections import defaultdict

def __log_missing():
    print('key added')
    return 0

class _CountMissing(object):
    def __init__(self):
        self.added = 0
    def __call__(self):
        self.added += 1
        return 0

CURRENT = {'green':12, 'blue': 3}
INCREMENTS = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9),
]

COUNTMISSING = _CountMissing()
RESULT = defaultdict(COUNTMISSING, CURRENT)
print('Before', dict(RESULT))

for key, amout in INCREMENTS:
    RESULT[key] += amout
print('After', dict(RESULT))
