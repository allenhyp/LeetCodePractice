class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maximum = cur = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                cur += 1
                maximum = max(maximum, cur)
            else:
                cur = 1
        return maximum
