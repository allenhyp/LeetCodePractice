from typing import List
from bisect import bisect_left
from collections import deque


def number_of_swaps_to_sort(nums: List[int]) -> int:
    pq = deque()
    res = 0
    for num in nums[::-1]:
        idx = bisect_left(pq, num)
        res += idx
        pq.insert(idx, num)
    return res
    # sorted_nums = sorted(nums)
    # res = 0
    # for num in nums:
    #     idx = bisect_left(sorted_nums, num)
    #     res += idx
    #     sorted_nums.pop(idx)
    # return res

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    res = number_of_swaps_to_sort(nums)
    print(res)
