#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""#49 in chapter7

Documentaion of
- module
- class
- method

"""

from pprint import pprint

def is_palindrome(word):
    """Return True if the given word is a palindrome."""
    return word == word[::-1]

class Documentaion(object):
    """Sample for class documentation. \
Documentaion of this class can be printed like 'print(Documentaion())'
    """

    def __init__(self):
        pass


    def __repr__(self):
        doc = Documentaion().__doc__
        return doc

pprint(Documentaion())

print('Is "level" a palindrome? : ', is_palindrome("level"))
print('Is "palindrome" a palindrome? : ', is_palindrome("palindrome"))
print('"たけやぶやけた"は回文か? : ', is_palindrome("たけやぶやけた"))
print('"たけやぶやけた"は回文か?(バイト列にエンコードした場合) : ', is_palindrome("たけやぶやけた".encode('utf-8')))
