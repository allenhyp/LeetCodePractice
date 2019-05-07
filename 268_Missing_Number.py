class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        summary = (0 + size) * (size + 1) // 2
        for n in nums:
            summary -= n
        return summary
