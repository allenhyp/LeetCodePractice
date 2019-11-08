class Solution:
    def singleNumber(self, nums: List[int]) -> int:
	    res = 0
        for n in nums:
            res ^= n
        return res


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return sum(set(nums)) * 2 - sum(nums)
