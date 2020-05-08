class Vector:
    """3D implementation of vector using __slots__.

    base
    >>> v = Vector(1, 2, 3)
    >>> x, y, z = v
    >>> print(x, y, z)
    1 2 3
    >>> v == Vector(1, 2, 4)
    False
    >>> v == Vector(1, 2, 3)
    True

    bonus 1
    >>> Vector(1, 2, 3) + Vector(4, 5, 6) == Vector(5, 7, 9)
    True
    >>> Vector(5, 7, 9) - Vector(3, 1, 2) == Vector(2, 6, 7)
    True
    """
    __slots__ = ('x', 'y', 'z')

    def __init__(self, x: float, y: float, z: float):
        self.x, self.y, self.z = x, y, z

    def __iter__(self):
        # required to work w/ multiple assignment
        yield self.x
        yield self.y
        yield self.z

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __ne__(self, other):
        return not (self == other)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
