#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests of lib.py"""

from unittest import TestCase, main
from lib import to_str

class UnitTestCase1(TestCase):
    def test_to_str_bytes(self):
        self.assertEqual('hello', to_str(b'hello'))
    def test_to_str_str(self):
        self.assertEqual('hello', to_str('hello'))    
    def test_to_str_bad(self):
        self.assertRaises(TypeError, to_str, object())

class UnitTestCase2(TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        self.value = 0
        print('__init__')

    def setUp(self):
        print('set up')

    def tearDown(self):
        print('tear down')

    def test_to_str_bytes(self):
        self.assertEqual(str(self.value), to_str(str(self.value).encode()))


    def test_to_str_str(self):
        self.assertEqual(str(self.value), to_str(str(self.value))) 


    def test_to_str_bad(self):
        self.assertRaises(TypeError, to_str, object())


if __name__ == '__main__':
    main()
