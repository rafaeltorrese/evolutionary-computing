from math import dist
from collections import namedtuple
from enum import Enum


class Point(Enum):
    A=(2, 4)
    B=(0, 5)
    C=(0, 10)
    D=(5, 10)
    E=(10, 10)
    F=(10, 5)
    G=(10, 0)
    H=(5, 0)


print(Point.A.value)

print(dist(Point.A.value, Point.B.value))