#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER3
"""

class GenericInputData(object):
    def read(self):
        raise NotImplementedError
    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError

class PathInputData(GenericInputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()

    @classmethod
    def generate_inputs(cls, config):
        import os
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))

class GenericWorker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError
    def reduce(self, other):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers

class LineCountWorker(GenericWorker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')
    def reduce(self, other):
        self.result += other.result

def execute(workers):
    from threading import Thread
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    first, rest = workers[0], workers[1:]
    for worker in rest:
        first.reduce(worker)
    return first.result

def mapreduce(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)

CONFIG = {'data_dir':"./../Ch3"}
RESULT = mapreduce(LineCountWorker, PathInputData, CONFIG)
print("There are", RESULT, 'lines')
