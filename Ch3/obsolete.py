#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER3
"""

class SimpleGradeBook(object):
    """
    Memory strudents' grades.
    """

    def __init__(self):
        self._grades = {}


    def add_student(self, name):
        """
        Add student name as a key of dictionary.
        """
        self._grades[name] = []


    def report_grade(self, name, score):
        """
        Append score in one's grades.
        """
        self._grades[name].append(score)


    def average_grade(self, name):
        """
        Calculate one's average grade.
        """
        grades = self._grades[name]
        return sum(grades) / len(grades)

class BySubjectGradeBook(object):
    """
    Memory strudents' grades by subjects.
    """

    def __init__(self):
        self._grades = {}


    def add_student(self, name):
        """
        Add student name as a key of dictionary.
        """
        self._grades[name] = {}


    def report_grade(self, name, subject, grade):
        """
        Append grade of the subject in one's grades.
        """
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(grade)

    def average_grade(self, name):
        """
        Calculate one's average grade.
        """
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count

class WeightedGradeBook(object):
    """
    Memory strudents' grades by subjects.
    """

    def __init__(self):
        self._grades = {}


    def add_student(self, name):
        """
        Add student name as a key of dictionary.
        """
        self._grades[name] = {}


    def report_grade(self, name, subject, grade, weight):
        """
        Append grade of the subject in one's grades.
        """
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append((grade, weight))

    def average_grade(self, name):
        """
        Calculate one's average grade.
        """
        by_subject = self._grades[name]
        sum_score, sum_count = 0, 0

        for subject, scores in by_subject.items():
            subject_avg, total_weith = 0, 0
        return 0

BOOK = SimpleGradeBook()
BOOK.add_student("Isaac Newton")
BOOK.report_grade("Isaac Newton", 90)

print(BOOK.average_grade("Isaac Newton"))

BOOK = BySubjectGradeBook()
BOOK.add_student("Albert Einstein")
BOOK.report_grade("Albert Einstein", 'Math', 75)
BOOK.report_grade("Albert Einstein", 'Math', 65)
BOOK.report_grade("Albert Einstein", 'Gym', 90)
BOOK.report_grade("Albert Einstein", 'Gym', 95)

print(BOOK.average_grade("Albert Einstein")) 