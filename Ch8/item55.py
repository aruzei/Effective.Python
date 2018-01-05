#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""#50 in chapter7"""

print('foo bar')
print('%s' % 'foo bar')

print(1)
print('1')

A = '\x41'
print(A)
print(repr(A))

print ('%r' % 5)
print ('%r' % '5')


class _OpaqueClass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class _BetterClass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'BetterClass(%d, %d)' % (self.x, self.y)

print(_OpaqueClass(1, 2))
print(_OpaqueClass(1, 2).__dict__)
print(_BetterClass(1, 2))
