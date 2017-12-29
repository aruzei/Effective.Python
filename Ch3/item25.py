#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER3
"""


class Parent(object):
    def __init__(self, value):
        self.value = value

class Child(Parent):
    def __init__(self):
        Parent.__init__(self, 5)

def __printvalue(expected, actual):
    print("Expected value : ", expected)
    print("Actual value   : ", actual.value)

class TimesTwo(Parent):
    def __init__(self, value):
        super().__init__(value)
        self.value *= 2

class PlusFive(Parent):
    def __init__(self, value):
        super().__init__(value)
        self.value += 5

class OneWay(TimesTwo, PlusFive):
    def __init__(self, value):
        super().__init__(value)

__printvalue(5, Child())
__printvalue(20, OneWay(5))
