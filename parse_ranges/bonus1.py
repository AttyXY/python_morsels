from typing import List

def parse_ranges(ranges: str) -> List[int]:
    """Returns an iterable of numbers, given a string containing
    ranges of numbers.

    >>> numbers = parse_ranges('100-10000')
    >>> next(numbers)
    100
    >>> next(numbers)
    101
    """
    iterable_range = []
    for r in ranges.split(','):
        first_num = int(r.split('-')[0])
        second_num = int(r.split('-')[1])

        # inclusive range
        iterable_range.extend([n for n in range(first_num, second_num + 1)])

    return iter(iterable_range)
