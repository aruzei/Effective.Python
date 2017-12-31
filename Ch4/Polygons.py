#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER4
"""

class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        if bases != (object,):
            if class_dict['sides'] < 3:
                raise ValueError('Polygons need 3+ sides')
        return type.__new__(meta, name, bases, class_dict)

class Polygon(object, metaclass=ValidatePolygon):
    sides = None

    @classmethod
    def __interior_angle(cls):
        return (cls.sides -2 ) * 180

class Triangle(Polygon):
    sides = 3

