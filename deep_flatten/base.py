from typing import List, Any

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
