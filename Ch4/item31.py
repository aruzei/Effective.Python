#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER4
"""

# from Grades import Grade
from Grades import Exam

EXAM1 = Exam()
EXAM1.math_grade = 71
# EXAM1.sciece_grade = 101
EXAM1.writting_grade = 81

EXAM2 = Exam()
EXAM2.math_grade = 100
EXAM2.sciece_grade = 92
# EXAM2.writting_grade = -1

print(EXAM1)
print(EXAM2)
