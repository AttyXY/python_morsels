from typing import List

def get_ranges(nums: List[int]) -> List[List[int]]:
    """Returns nums with consecutive numbers grouped together.
    Assumes: nums is sorted from least to greatest.

    >>> get_ranges([1, 2, 3, 4, 5, 6, 7, 8])
    [[1, 2, 3, 4, 5, 6, 7, 8]]
    >>> get_ranges([1, 2, 3, 5, 6, 7, 8, 10, 11])
    [[1, 2, 3], [5, 6, 7, 8], [10, 11]]
    >>> get_ranges([])
    [[]]
    >>> get_ranges([1, 1, 2, 2, 3, 4, 4, 7, 7, 8, 9])
    [[1, 2], [1, 2, 3, 4], [4], [7], [7, 8, 9]]
    >>> get_ranges([1, 1, 1, 2, 2, 2])
    [[1, 2], [1, 2], [1, 2]]
    >>> get_ranges([1, 1, 1, 2, 2, 2, 3, 3, 4, 4])
    [[1, 2], [1, 2, 3, 4], [1, 2, 3, 4]]
    """
    ranges = [[]]
    try:
        ranges[-1].append(nums[0])
    except IndexError:
        return ranges

    for i in range(1, len(nums)):
        prev_num = nums[i - 1]
        curr_num = nums[i]
        if curr_num == prev_num:
            for r in reversed(ranges):
                if curr_num == r[-1] + 1:
                    # add second consecutive duplicate to previous range
                    r.append(curr_num)
                    break
            else:
                ranges.append([curr_num])
        elif curr_num == prev_num + 1:
            ranges[-1].append(curr_num)
        else:
            ranges.append([curr_num])

    return ranges