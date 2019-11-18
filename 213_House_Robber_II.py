class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        def rob(nums):
            a = b = 0
            for n in nums:
                a, b = max(b + n, a), a
            return max(a, b)
        return max(rob(nums[:-1]), rob(nums[1:]))
