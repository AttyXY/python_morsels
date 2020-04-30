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
    """
    __slots__ = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __iter__(self):
        # required to work w/ multiple assignment
        yield self.x
        yield self.y
        yield self.z

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y and self.z == other.z)

    def __ne__(self, other):
        return not (self == other)
