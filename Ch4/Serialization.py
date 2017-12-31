#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER4
"""

import json

class Serializable(object):
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({
            'class': self.__class__.__name__,
            'args': self.args,
        })

    def __repr__(self):
        args = self.args
        name = str(self.__class__.__name__)
        return '%s%s' % (name, args)

class Deserialization(object):
    registory = {}

    @classmethod
    def register_class(cls, target_class):
        cls.registory[target_class.__name__] = target_class

    @classmethod
    def deserialize(cls, serializable_json):
        params = json.loads(serializable_json)
        name = params['class']
        target_class = cls.registory[name]
        return target_class(*params['args'])

class Registered(type):
    """
    Register for Deserialization
    """
    def __new__(meta, name, bases, class_dict):
        c = type.__new__(meta, name, bases,class_dict)
        Deserialization.register_class(c)
        return c
class RegisterdSerializable(Serializable, metaclass=Registered):
    pass