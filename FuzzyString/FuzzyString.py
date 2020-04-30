
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
    """
    def __eq__(self, other: str):
        return self.lower() == other.lower()

    def __ne__(self, other: str):
        return not self.__eq__(other)

    def __lt__(self, other: str):
        return self.lower() < other.lower()

    def __gt__(self, other: str):
        return self.lower() > other.lower()
