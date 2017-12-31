#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER4
"""


from Serialization import Serializable
from Serialization import RegisterdSerializable
from Serialization import Deserialization

class Point2D(Serializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

class Vector3D(RegisterdSerializable):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.x = x
        self.y = y
        self.z = z

Deserialization.register_class(Point2D)

P2D = Point2D(1,2)
Deserialization.register_class(Point2D)

print(P2D)
D2 = P2D.serialize()
print(Deserialization.deserialize(D2))

V3D = Vector3D(3, 4, 5)
print(V3D)
D3 = V3D.serialize()
print(Deserialization.deserialize(D3))
