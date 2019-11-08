class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (sum(set(nums)) * 3 - sum(nums)) // 2

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a, b = 0, 0
        for n in nums:
            a = (a ^ n) & ~b
            b = (b ^ n) & ~a
        return a