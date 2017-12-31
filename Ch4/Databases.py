#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER4
"""


class LazyDB(object):
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = 'Value for %s' % name
        setattr(self, name, value)
        return value


class LoggingLazyDB(LazyDB):
    def __getattr__(self, name):
        print('Called __getattr__(%s)' % name)
        return super().__getattr__(name)

class ValidatingDB(object):
    def __init__(self):
        self.exists = 5
    
    def __getattribute__(self, name):
        print('Called __getattribute__(%s)' % name)
        try:
            return super().__getattribute__(name)
        except AttributeError:
            value = 'Value for %s' % name
            setattr(self, name, value)
            return value

class SavingDB(object):
    def __setattr__(self, name, value):
        super().__setattr__(name, value)

class LoggingSavingDB(SavingDB):
    def __setattr__(self, name, value):
        print('Called __setattr__(%s, %r)' % (name, value))
        super().__setattr__(name, value)

class DictionayDB(object):
    def __init__(self, data):
        self._data = data
    def __getattribute__(self, name):
        print('Called __getattribute__(%s)' % name)
        # To avoide infinite loop
        data_dict = super().__getattribute__('_data')
        return data_dict[name]        