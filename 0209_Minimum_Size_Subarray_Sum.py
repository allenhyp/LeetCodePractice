class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        res = len(nums) + 1
        curr = 0
        while r < len(nums):
            curr += nums[r]
            while curr >= target:
                res = min(res, r-l+1)
                curr -= nums[l]
                l += 1
            r += 1
            
        return res if res < len(nums) + 1 else 0
