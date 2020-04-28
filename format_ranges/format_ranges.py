from typing import List


def format_ranges(nums: List[int]) -> str:
    """Returns nums with consecutive numbers grouped together.

    base
    >>> format_ranges([1, 2, 3, 4, 5, 6, 7, 8])
    '1-8'
    >>> format_ranges([1, 2, 3, 5, 6, 7, 8, 10, 11])
    '1-3,5-8,10-11'

    custom
    >>> format_ranges([])
    ''
    """
    # First num
    try:
        last_num = nums[0]
        ranges = f"{last_num}"
    except IndexError:
        return ""

    # In-between nums
    for n in nums[1:-1]:
        if n != last_num + 1:
            ranges += f"-{last_num},{n}"
        last_num = n

    # Last num
    n = nums[-1]
    if n != last_num + 1:
        ranges += f"-{last_num},{n}"
    else:
        ranges += f"-{n}"

    return ranges
