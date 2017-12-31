#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER4
"""

from weakref import WeakKeyDictionary

class Grade(object):
    """
    Property descripor of Grade
    """
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self._values.get(instance, 0)
    def __set__(self, instance, value):
        if not 0 <= value <= 100:
            raise ValueError('Grade must be between 0 and 100')
        self._values[instance] = value

class Exam(object):
    """
    Results of grades
    """
    math_grade = Grade()
    writting_grade = Grade()
    sciece_grade = Grade()

    def __repr__(self):
        return "Math = %3d, Science = %3d, Writting = %3d" \
         % (self.math_grade, self.sciece_grade, self.writting_grade)
