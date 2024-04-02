class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [float('-inf')] + nums + [float('-inf')]
        l, r = 1, len(nums) - 2
        while l <= r:
            m = (l+r)//2
            if nums[m-1] < nums[m] > nums[m+1]:
                return m-1
            if nums[m-1] < nums[m] < nums[m+1]:
                l = m+1
            else:
                r = m
        return -1
