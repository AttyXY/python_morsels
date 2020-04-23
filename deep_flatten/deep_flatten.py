from typing import List

def deep_flatten(lst: List[List]):
    """Returns a flattened version of lst

    >>> deep_flatten([[(1, 2), (3, 4)], [(5, 6), (7, 8)]])
    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> deep_flatten([[1, [2, 3]], 4, 5])
    [1, 2, 3, 4, 5]
    """
    flattened_list = []
    for elem in lst:
        if not hasattr(elem, "__iter__"):
            flattened_list.append(elem)
        else:
            flattened_list.append(deep_flatten(elem))

    return flattened_list
