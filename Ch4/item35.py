#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER4
"""


from Fields import Customer

C = Customer()

print(repr(C.first_name), C.__dict__)
C.first_name = "Euclid"
print(repr(C.first_name), C.__dict__)
