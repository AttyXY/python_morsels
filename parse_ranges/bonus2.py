from typing import List

def parse_ranges(ranges: str) -> List[int]:
    """Returns an iterable of numbers, given a string containing
    ranges of numbers.

    >>> list(parse_ranges('0,4-8,20,43-45'))
    [0, 4, 5, 6, 7, 8, 20, 43, 44, 45]
    """
    iterable_range = []
    for r in ranges.split(','):
        first_num = int(r.split('-')[0])
        try:
            second_num = int(r.split('-')[1])
        except IndexError:
            second_num = first_num

        # inclusive range
        iterable_range.extend([n for n in range(first_num, second_num + 1)])

    return iter(iterable_range)
