
class FuzzyString(str):
    """String with case-insensitive comparison operators

    base
    >>> greeting = FuzzyString('Hey TREY!')
    >>> greeting == 'hey Trey!'
    True
    >>> greeting == 'heyTrey'
    False
    >>> greeting
    'Hey TREY!'

    bonus 1: lt, gt
    >>> o_word = FuzzyString('Octothorpe')
    >>> 'hashtag' < o_word
    True
    >>> 'hashtag' > o_word
    False

    custom
    >>> test = FuzzyString('B')
    >>> test == 'b'
    True
    >>> test == 'A'
    False

    >>> test < 'b'
    False
    >>> test < 'b'
    False
    >>> test < 'a'
    False
    >>> test > 'a'
    True

    >>> test <= 'b'
    True
    >>> test >= 'b'
    True
    >>> test <= 'a'
    False
    >>> test >= 'a'
    True

    """
    def __eq__(self, other: str):
        return self.lower() == other.lower()

    def __lt__(self, other: str):
        return self.lower() < other.lower()

    def __gt__(self, other: str):
        return self.lower() > other.lower()

    def __ne__(self, other: str):
        return not self.__eq__(other)

    def __le__(self, other: str):
        return self.__eq__(other) or self.__lt__(other)

    def __ge__(self, other: str):
        return self.__eq__(other) or self.__gt__(other)
