from typing import List, Any, Iterable


def deep_flatten(lst: List[Any]) -> List[Any]:
    """Returns a flattened version of lst

    Base: Accept lists
    >>> deep_flatten([[(1, 2), (3, 4)], [(5, 6), (7, 8)]])
    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> deep_flatten([[1, [2, 3]], 4, 5])
    [1, 2, 3, 4, 5]
    """
    flattened_list = []

    for elem in lst:
        try:
            flattened_list.extend(deep_flatten(elem))
        except TypeError:
            flattened_list.append(elem)

    return flattened_list


# Bonus 1
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


# Bonus 2
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
        try:
            yield from deep_flatten(elem)
        except TypeError:
            yield elem


# Bonus 3
def deep_flatten(iterable: Iterable) -> Iterable:
    """Returns a flattened version of iterable

    Bonus 3: Accept all iterables, including strings
    >>> list(deep_flatten([['apple', 'pickle'], ['pear', 'avocado']]))
    ['apple', 'pickle', 'pear', 'avocado']
    """
    flattened_list = []
    for elem in iterable:
        if isinstance(elem, str):
            flattened_list.append(elem)
        else:
            try:
                flattened_list.extend(deep_flatten(elem))
            except TypeError:
                flattened_list.append(elem)

    return flattened_list
