#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER6
"""

import logging
from contextlib import contextmanager

def _myfunc():
    logging.debug('Some debug data')
    logging.error('Error log here')
    logging.debug('More debug data')

@contextmanager
def _debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)

    try:
        yield
    finally:
        logger.setLevel(old_level)

@contextmanager
def log_level(level, name):
    _logger = logging.getLogger(name)
    old_level = _logger.getEffectiveLevel()
    _logger.setLevel(level)
    try:
        yield _logger
    finally:
        _logger.setLevel(old_level)

with _debug_logging(logging.DEBUG):
    print('Inside:')
    _myfunc()

print('After')
_myfunc()

with log_level(logging.DEBUG, 'my-log') as logger:
    logger.debug('This is my message!')
    logging.debug('This will not print')
