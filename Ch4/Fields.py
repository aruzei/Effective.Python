#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER4
"""


class Field(object):
    def __init__(self):
        self.name = None
        self.internal_name = None
    
    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, '')
    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)
  
class MetaDatabaseRow(type):
    def __new__(meta, name, bases, class_dict):
        for key, value in class_dict.items():
            if isinstance(value,Field):
                value.name = key
                value.internal_name = '_' + key
        c = type.__new__(meta, name, bases, class_dict)
        return c

class DatabaseRow(object,metaclass=MetaDatabaseRow):
    pass

class Customer(DatabaseRow):

    first_name = Field()
    last_name = Field()
