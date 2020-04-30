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

    bonus 3: normalize unicode characters when checking for equality
    >>> ss = FuzzyString('ss')
    >>> '\u00df' == ss
    True
    >>> e = FuzzyString('\u00e9')
    >>> '\u0065\u0301' == e
    True
    >>> '\u0301' in e
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
    def parse_unicode(func):
        """Normalizes unicode arguments to func"""
        def normalize(*args, **kwargs):
            import unicodedata
            # default to NFKD:
            #   http://www.unicode.org/reports/tr15/#Normalization_Forms_Table
            return func(*[unicodedata.normalize("NFKD", arg) for arg in args],
                        *{k: unicodedata.normalize("NFKD", v) for k,v in kwargs})

        return normalize


    @parse_unicode
    def __eq__(self, other: str):
        return self.casefold() == other.casefold()

    @parse_unicode
    def __lt__(self, other: str):
        return self.casefold() < other.casefold()

    @parse_unicode
    def __gt__(self, other: str):
        return self.casefold() > other.casefold()

    @parse_unicode
    def __ne__(self, other: str):
        return not self.__eq__(other)

    @parse_unicode
    def __le__(self, other: str):
        return self.__eq__(other) or self.__lt__(other)

    @parse_unicode
    def __ge__(self, other: str):
        return self.__eq__(other) or self.__gt__(other)

    @parse_unicode
    def __contains__(self, other: str):
        return other.casefold() in self.casefold()

    @parse_unicode
    def __add__(self, other: str):
        return FuzzyString(super().__add__(other))
