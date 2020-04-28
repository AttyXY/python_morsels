from typing import List


def format_ranges(nums: List[int]) -> str:
    """Returns string representation of ranges of consecutive numbers.

    base
    >>> format_ranges([1, 2, 3, 4, 5, 6, 7, 8])
    '1-8'
    >>> format_ranges([1, 2, 3, 5, 6, 7, 8, 10, 11])
    '1-3,5-8,10-11'

    custom
    >>> format_ranges([])
    ''
    """
    ranges = [[]]
    try:
        ranges[-1].append(nums[0])
    except IndexError:
        return ""   # empty list

    for i in range(1, len(nums)):
        prev_num = nums[i - 1]
        curr_num = nums[i]
        if curr_num != prev_num + 1:
            ranges.append([curr_num])
        else:
            ranges[-1].append(curr_num)

    return ','.join([f"{consecutives[0]}-{consecutives[-1]}" for consecutives in ranges])
