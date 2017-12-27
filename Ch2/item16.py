#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER2
"""

def __index_word_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

SENTENCE = "Four socre and seven years ago..."

print(list(__index_word_iter(SENTENCE)))
