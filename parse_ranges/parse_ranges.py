from typing import List

# Base
def parse_ranges(ranges: str) -> List[int]:
    """Returns an iterable of numbers, given a string containing
    ranges of numbers.

    >>> parse_ranges('1-2,4-4,8-10')
    [1, 2, 4, 8, 9, 10]
    >>> parse_ranges('0-0, 4-8, 20-20, 43-45')
    [0, 4, 5, 6, 7, 8, 20, 43, 44, 45]
    """
    iterable_range = []
    for r in ranges.split(','):
        first_num = int(r.split('-')[0])
        second_num = int(r.split('-')[1])

        # inclusive range
        iterable_range.extend([n for n in range(first_num, second_num + 1)])

    return iterable_range


# Bonus 1
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


# Bonus 2
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


# Bonus 3
def parse_ranges(ranges: str) -> List[int]:
    """"Returns an iterable of numbers, given a string containing
    ranges of numbers.

    >>> list(parse_ranges('0, 4-8, 20->exit, 43-45'))
    [0, 4, 5, 6, 7, 8, 20, 43, 44, 45]
    """
    iterable_range = []
    for r in ranges.split(','):
        first_num = int(r.split('-')[0])
        try:
            second_num = int(r.split('-')[1])
        except (IndexError, TypeError, ValueError):
            second_num = first_num

        # inclusive range
        iterable_range.extend([n for n in range(first_num, second_num + 1)])

    return iter(iterable_range)
