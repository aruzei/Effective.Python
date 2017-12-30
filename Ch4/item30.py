#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER3
"""

from Buckets import Bucket
from Buckets import fill
from Buckets import deduct

def print_logger(message):
    print(message)


BUCKET = Bucket(60, logger=print_logger)
fill(BUCKET, 100)
deduct(BUCKET, 99)
deduct(BUCKET, 10)
