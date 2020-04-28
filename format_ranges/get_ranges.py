from typing import List

def get_ranges(nums: List[int]) -> List[List[int]]:
    """Returns nums with consecutive numbers grouped together.

    >>> get_ranges([1, 2, 3, 4, 5, 6, 7, 8])
    [[1, 2, 3, 4, 5, 6, 7, 8]]
    >>> get_ranges([1, 2, 3, 5, 6, 7, 8, 10, 11])
    [[1, 2, 3], [5, 6, 7, 8], [10, 11]]
    >>> get_ranges([])
    [[]]
    """
    ranges = [[]]
    try:
        ranges[-1].append(nums[0])
    except IndexError:
        return ranges

    for i in range(1, len(nums)):
        prev_num = nums[i - 1]
        curr_num = nums[i]
        if curr_num != prev_num + 1:
            ranges.append([curr_num])
        else:
            ranges[-1].append(curr_num)

    return ranges