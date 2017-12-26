#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER1
"""

FLAVORS = ['vanilla', 'chocolate', 'pecan', 'strawberry']

# [pylint] C0200:Consider using enumerate instead of iterating with range and len
for i in range(len(FLAVORS)):
    flavor = FLAVORS[i]
    print('%d: %s is delicious' % (i+1, flavor))

for i, flavor in enumerate(FLAVORS):
    print('%d: %s is delicious' % (i+1, flavor))
# We can start index from one.
for i, flavor in enumerate(FLAVORS, 1):
    print('%d: %s is delicious' % (i, flavor))
 