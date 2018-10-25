class Solution:
    def maxCrossSectionSum(self, nums, l, m, r):
        cur_sum, l_max = 0, -sys.maxsize - 1
        for i in range(m, l - 1, -1):
            cur_sum += nums[i]
            if cur_sum > l_max:
                l_max = cur_sum
        cur_sum, r_max = 0, -sys.maxsize - 1
        for i in range(m + 1, r + 1):
            cur_sum += nums[i]
            if cur_sum > r_max:
                r_max = cur_sum
        return l_max + r_max


    def maxSubArraySum(self, nums, l, r):
        if (l == r):
            return nums[l]
        m = (l + r) // 2
        return max(self.maxSubArraySum(nums, l, m),
                   self.maxSubArraySum(nums, m + 1, r),
                   self.maxCrossSectionSum(nums, l, m, r))


    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.maxSubArraySum(nums, 0, len(nums) - 1)
