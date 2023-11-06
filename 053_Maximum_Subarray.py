class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return nums[0]
        dp = [0] * size
        dp[0] = nums[0]
        for i in range(1, size):
            dp[i] = nums[i] + (dp[i - 1] if dp[i - 1] > 0 else 0)
        return max(dp)


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


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax, maxTillNow = 0, -inf
        for i in range(len(nums)):
            curMax = max(nums[i], nums[i] + curMax)
            maxTillNow = max(maxTillNow, curMax)
            
        return maxTillNow
