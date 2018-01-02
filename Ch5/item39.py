#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER5
"""

from collections import deque
from queue import Queue

from threading import Lock
from threading import Thread
from time import sleep

class _Queue(object):
    def __init__(self):
        self.items = deque()
        self.lock = Lock()


    def put(self, item):
        """
        Put item to queue
        """
        with self.lock:
            self.items.append(item)


    def get(self):
        """
        Pop the most left item from queue
        """
        with self.lock:
            self.items.popleft()

class _Worker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.polled_count = 0
        self.work_done = 0


    def run(self):
        """
        Pop the item from in_queue and then run it, finally put the result to out_queue
        """
        while True:
            self.polled_count += 1
            try:
                item = self.in_queue.get()
            except IndexError:
                sleep(0.01) # no work
            else:
                result = self.func(item)
                self.out_queue.put(result)
                self.work_done += 1

class _ClosableQueue(Queue):
    SENTINEL = object()

    def close(self):
        "Add an item to close queue"
        self.put(self.SENTINEL)

    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.SENTINEL:
                    return
                yield item
            finally:
                self.task_done()

class _StoppableWorker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue


    def run(self):
        for item in self.in_queue:
            result = self.func(item)
            self.out_queue.put(result)


def _do_something(item):
    pass

# Q1 = _Queue()
# Q2 = _Queue()
# Q3 = _Queue()
# Q4 = _Queue()

# THRADS = [
#     _Worker(_do_something, Q1, Q2),
#     _Worker(_do_something, Q2, Q3),
#     _Worker(_do_something, Q3, Q4),
# ]

# for t in THRADS:
#     t.start()
# for _ in range(1000):
#     Q1.put(object())

# while len(Q4.items) < 1000:
#     pass

# PROCESSED = len(Q4.items)

# POLLED = sum(t.polled_count for t in THRADS)
# print('Processed', PROCESSED, 'items after polling', POLLED, 'times')

# Q = Queue(1)
# def _consumer():
#     print("Consumer waiting")
#     Q.get()
#     print('Consumer working')
#     Q.task_done()
#     print('Consumer done')

# T = Thread(target=_consumer)
# T.start()

# Q.put(object())
# print('Producer waiting')
# T.join()
# print('Producer done')

Q1 = _ClosableQueue()
Q2 = _ClosableQueue()
Q3 = _ClosableQueue()
Q4 = _ClosableQueue()

THRADS = [
    _StoppableWorker(_do_something, Q1, Q2),
    _StoppableWorker(_do_something, Q2, Q3),
    _StoppableWorker(_do_something, Q3, Q4),
]

for t in THRADS:
    t.start()
for _ in range(1000):
    Q1.put(object())

def _stop(q):
    q.close()
    q.join()
_stop(Q1)
_stop(Q2)
_stop(Q3)

# Q1.close()
# Q1.join()
# Q2.close()
# Q2.join()
# Q3.close()
# Q3.join()

print(Q4.qsize(), 'items finished')
