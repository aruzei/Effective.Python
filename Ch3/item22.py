#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER3
"""

import collections    

Grade = collections.namedtuple('Grade',('score', 'weight'))

class Subject(object):
    """
    Manage score of subject
    """

    def __init__(self):
        self._grades = []


    def report_grade(self, score, weight):
        """
        Append score and weight in one's grades.
        """
        self._grades.append(Grade(score, weight))


    def average_grade(self):
        """
        Calculate weighted average of grades.
        """
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight

class Student(object):
    """
    Manege student
    """

    def __init__(self):
        self._subjects = {}


    def subject(self, name):
        """
        Return student's subject.
        """
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]

    def average_grade(self):
        """
        Calculate one's average grade.
        """
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count

class _GradeBook(object):
    def __init__(self):
        self._students = {}
    def student(self, name):
        """
        Get student listed in gradebook.
        """
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]

BOOK = _GradeBook()
ALBERT = BOOK.student("Albert Einstein")
MATH = ALBERT.subject("Math")
MATH.report_grade(80, 0.1)
MATH.report_grade(100, 0.9)

print(ALBERT.average_grade())
