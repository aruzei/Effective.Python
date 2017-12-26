#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER1
"""

HANDLE = open('shit_jis.txt', encoding='utf-8')
try:
    SENTENCE = HANDLE.read()
except UnicodeDecodeError as ex:
    print(ex)
finally:
    HANDLE.close()

HANDLE = open('utf-8.txt', encoding='utf-8')
try:
    SENTENCE = HANDLE.read()
except UnicodeDecodeError as ex:
    print(ex)
else:
    print(SENTENCE)
finally:
    HANDLE.close()
