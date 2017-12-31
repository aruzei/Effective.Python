#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER4
"""

from Databases import LazyDB
from Databases import LoggingLazyDB
from Databases import ValidatingDB
from Databases import LoggingSavingDB
from Databases import DictionayDB

def __my_print(database):
    print(database.__class__)
    print(database.__dict__)
    print(database.foo)
    print(database.__dict__)
    print(database.foo)
    print()

DB1 = LazyDB()
__my_print(DB1)

DB2 = LoggingLazyDB()
__my_print(DB2)

DB3 = ValidatingDB()
__my_print(DB3)


DB4 = LoggingSavingDB()
DB4.foo = 5
DB4.foo = 7

DB5 = DictionayDB({'foo': 3})
DB5.foo
