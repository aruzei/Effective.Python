#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER1
"""

L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(L[:])     # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(L[:5])    # ['a', 'b', 'c', 'd', 'e']
print(L[:-1])   # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(L[4:])    #                     ['e', 'f', 'g', 'h']
print(L[-3:])   #                          ['f', 'g', 'h']
print(L[2:5])   #           ['c', 'd', 'e']
print(L[2:-1])  #           ['c', 'd', 'e', 'f', 'g']
print(L[-3:-1]) #                          ['f', 'g']

print()

BEFORE = L[4:]
AFTER = BEFORE[:]
AFTER[1] = 99

print('Before    : ', BEFORE)
print('After     : ', AFTER)
print('No change : ', L)
