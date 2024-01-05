from collections import Counter
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        map = Counter(nums)
        ret = 0
        for count in map.values():
            if count == 1:
                return -1
            if count % 3 == 0:
                ret += count // 3
            elif count % 3 == 1:
                ret += (count - 1) // 3 + 1
            else:
                ret += count // 3 + 1
        return ret
