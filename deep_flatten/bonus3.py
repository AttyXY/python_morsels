from typing import Iterable

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
        elif hasattr(elem, "__iter__"):
            flattened_list.extend(deep_flatten(elem))
        else:
            flattened_list.append(elem)

    return flattened_list
