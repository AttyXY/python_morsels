from __future__ import annotations
from numbers import Number
from dataclasses import dataclass


@dataclass(frozen=True)
class Vector:
    """3D immutable implementation of Vector.

    base
    >>> v = Vector(1, 2, 3)
    >>> x, y, z = v
    >>> print(x, y, z)
    1 2 3
    >>> v == Vector(1, 2, 4)
    False
    >>> v == Vector(1, 2, 3)
    True

    bonus 1: support addition + subtraction
    >>> Vector(1, 2, 3) + Vector(4, 5, 6) == Vector(5, 7, 9)
    True
    >>> Vector(5, 7, 9) - Vector(3, 1, 2) == Vector(2, 6, 7)
    True

    bonus 2: support multiplication + division
    >>> 3 * Vector(1, 2, 3) == Vector(3, 6, 9)
    True
    >>> Vector(1, 2, 3) * 2 == Vector(2, 4, 6)
    True
    >>> Vector(1, 2, 3) / 2 == Vector(0.5, 1, 1.5)
    True

    bonus 3: make immutable
    >>> v = Vector(1, 2, 3)
    >>> v.x = 4     # #doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    dataclasses.FrozenInstanceError: ...
    """
    x: Number
    y: Number
    z: Number

    __slots__ = ('x', 'y', 'z')
    def __iter__(self):
        # required to work w/ multiple assignment
        yield self.x
        yield self.y
        yield self.z

    def __eq__(self, other: Vector) -> bool:
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __ne__(self, other: Vector) -> bool:
        return not (self == other)

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError("Vector can only be added to another Vector.")
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError("Vector can only be subtracted from another Vector.")
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar: Number) -> Vector:
        if not isinstance(scalar, Number):
            raise TypeError("Vector can only be multiplied by a scalar.")
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    __rmul__ = __mul__

    def __truediv__(self, scalar: Number) -> Vector:
        if not isinstance(scalar, Number):
            raise TypeError("Vector can only be divided by a scalar.")
        return Vector(self.x / scalar, self.y / scalar, self.z / scalar)
