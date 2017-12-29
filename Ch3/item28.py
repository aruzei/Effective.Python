#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER3
"""


class FrequencyList(list):
    def __init__(self, members):
        super().__init__(members)
    def frequency(self):
        counts = {}
        for item in self:
            counts.setdefault(item,0)
            counts[item] +=1
        return counts

FOO = FrequencyList(['a', 'b', 'c', 'a'])
print(FOO.frequency())

class BinaryNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class IndexableNode(BinaryNode):
    def _search(self, count, index):
        found = None
        if self.left:
            found, count = self.left._search(count, index)
        if not found and count == index:
            found = self
        else:
            count += 1
        if not found and self.right:
            found, count = self.right._search(count, index)
        return found, count
        # Returns (found, count)

    def __getitem__(self, index):
        found, _ = self._search(0, index)
        if not found:
            raise IndexError('Index out of range')
        return found.value

BAR = IndexableNode(
    10,
    left=IndexableNode(
        5,
        left=IndexableNode(2),
        right=IndexableNode(
            6, right=IndexableNode(7))),
    right=IndexableNode(
        15, left=IndexableNode(11)))
print(BAR[0])
print(BAR[1])
print(BAR[2])

class SequenceNode(IndexableNode):
    def __len__(self):
        _, count = self._search(0, None)
        return count
HOGE = SequenceNode(
    10,
    left=SequenceNode(
        5,
        left=SequenceNode(2),
        right=SequenceNode(
            6, right=SequenceNode(7))),
    right=SequenceNode(
        15, left=SequenceNode(11)))
print(len(HOGE))


from collections.abc import Sequence
class BetterNode(SequenceNode,Sequence):
    pass
HUGA = BetterNode(
    10,
    left=BetterNode(
        5,
        left=BetterNode(2),
        right=BetterNode(
            6, right=BetterNode(7))),
    right=BetterNode(
        15, left=BetterNode(11)))
print(HUGA.index(7))
print(HUGA.count(10))
