from typing import Iterable

def deep_flatten(iterable: Iterable) -> Iterable:
    """Returns a flattened version of iterable

    Bonus 1: Accept all iterables but strings
    >>> sorted(deep_flatten({(1, 2), (3, 4), (5, 6), (7, 8)}))
    [1, 2, 3, 4, 5, 6, 7, 8]
    """
    flattened_list = []
    for elem in iterable:
        try:
            flattened_list.extend(deep_flatten(elem))
        except TypeError:
            flattened_list.append(elem)

    return flattened_list
