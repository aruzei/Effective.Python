#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER3
"""


class MyObject(object):
    def __init__(self):
        self.public_value = "public"
        self.__private_value = "private"
FOO = MyObject()

print(FOO.public_value)
print(FOO._MyObject__private_value) # We can hack private field.
