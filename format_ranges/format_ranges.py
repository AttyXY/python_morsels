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
    ranges = []
    try:
        ranges.append(str(nums[0]))
    except IndexError:
        return ""   # empty list

    for i in range(1, len(nums)):
        prev_num = nums[i - 1]
        curr_num = nums[i]
        if curr_num != prev_num + 1:
            ranges[-1] = f"{ranges[-1]}-{prev_num}"
            ranges.append(str(curr_num))
        elif i == len(nums) - 1:
            ranges[-1] = f"{ranges[-1]}-{curr_num}"


    return ','.join(ranges)
