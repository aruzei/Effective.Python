#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER5
"""

from threading import Thread
from threading import Lock

from Profiles import profile_func

class _Counter(object):
    def __init__(self):
        self.count = 0

    def increment(self, offset):
        """
        Increment count by offset
        """
        self.count += offset

class _LockedCounter(object):
    def __init__(self):
        self.lock = Lock()
        self.count = 0

    def increment(self, offset):
        """
        Increment count by offset while locking counter
        """
        with self.lock:
            self.count += offset

def _worker(sensor_index, how_many, counter):  
    for _ in range(how_many):
        counter.increment(1)

def _run_threads(func, how_many, counter):
    threads = []
    for i in range(5):
        args = (i, how_many, counter)
        thread = Thread(target=func, args=args)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

HOW_MANY = 10**5

def _run(counter):
    _run_threads(_worker, HOW_MANY, counter)
    print('Counter should be %d, found %d' % (5 * HOW_MANY, counter.count))

def _run1():
    _run(_Counter())

def _run2():
    _run(_LockedCounter())

# Lock results in delaying the execution time.
profile_func(_run1) # 211 function calls in 0.128 seconds
profile_func(_run2) # 212 function calls in 2.404 seconds
