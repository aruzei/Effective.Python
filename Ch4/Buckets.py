#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER3
"""

from datetime import timedelta
from datetime import datetime

class Bucket(object):
    def __init__(self, period, logger=None):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.max_quota = 0
        self.quota_comsumed = 0
        self.logger = logger

    def __repr__(self):
        return "Bucket(max_quota=%d, quota_comsumed=%d)" % (self.max_quota, self.quota_comsumed)

    @property
    def quota(self):
        return self.max_quota - self.quota_comsumed

    @quota.setter
    def quota(self, amount):
        delta = self.max_quota - amount
        if amount == 0:
            self.quota_comsumed = 0
            self.max_quota = 0
        elif delta < 0:
            assert self.quota_comsumed == 0
            self.max_quota = amount
        else:
            assert self.max_quota >= self.quota_comsumed
            self.quota_comsumed += delta

        self.logger(self)

def fill(bucket, amount):
    now = datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = 0
    bucket.quota += amount


def deduct(bucket, amount):
    now = datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        return False
    if bucket.quota - amount < 0:
        return False
    bucket.quota -= amount
    return True
