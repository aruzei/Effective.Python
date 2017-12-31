#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER4
"""

from Registors import VolatageRegistance
from Registors import BoundedRegistance
from Registors import ImmutableRegistance

REGISTOR = VolatageRegistance(1e3)
REGISTOR.voltage = 10
print("%5r amps" % REGISTOR.current)

BOUNDED = BoundedRegistance(10e3)
try:
    BOUNDED.ohms = 0
except ValueError as ex:
    print(ex)

IMUUTABLE = ImmutableRegistance(5e2)
try:
    IMUUTABLE.ohms = 10
except AttributeError as ex:
    print(ex)
