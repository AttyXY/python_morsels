from typing import Iterable

def deep_flatten(iterable: Iterable) -> Iterable:
    """Returns a flattened version of iterable

    Bonus 2: Loops lazily
    >>> numbers_and_words = enumerate([99, 98, 97])
    >>> flattened = deep_flatten(numbers_and_words)
    >>> next(flattened)
    0
    >>> next(flattened)
    99
    >>> next(numbers_and_words)
    (1, 98)
    """
    for elem in iterable:
        if hasattr(elem, "__iter__"):
            yield from deep_flatten(elem)
        else:
            yield elem
