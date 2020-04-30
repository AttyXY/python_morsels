
class FuzzyString(str):
    """String with case-insensitive comparison operators

    tests
    -----
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

    bonus 2: string concatenation and 'in'
    >>> o_word = FuzzyString('Octothorpe')
    >>> 'OCTO' in o_word
    True
    >>> new_string = o_word + ' (aka hashtag)'
    >>> new_string == 'octothorpe (AKA hashtag)'
    True

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

    >>> 'a' in test
    False
    >>> type(new_string)
    <class 'fuzzystring.FuzzyString'>
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

    def __contains__(self, other: str):
        return other.lower() in self.lower()

    def __add__(self, other: str):
        return FuzzyString(super().__add__(other))
