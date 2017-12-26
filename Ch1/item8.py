#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER1
"""

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
FLAT = [x for row in M for x in row]
print(FLAT)

SQUARES = [[x ** 2 for x in row] for row in M]
print(SQUARES)

MULTIPLE_MATRIX = [M, M]
print(MULTIPLE_MATRIX)

FLAT_HARD_TO_READ = [x for subMatrix in MULTIPLE_MATRIX for row in subMatrix for x in row]
print(FLAT_HARD_TO_READ)

ZERO_NINE = list(range(0, 10, 1))
A = [x for x in ZERO_NINE if x > 4 if x % 2 == 0]
B = [x for x in ZERO_NINE if x > 4 and x % 2 == 0]

print(A)
print(B)

FILTERED = [[x for x in row if x % 3 == 0] for row in M if sum(row) >= 10]
print(FILTERED)
