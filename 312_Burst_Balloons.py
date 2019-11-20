class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        size = len(nums)
        dp = [[0] * size for _ in range(size)]
        for k in range(2, size):
            for left in range(0, size - k):
                right = left + k
                for i in range(left + 1, right):
                    dp[left][right] = max(dp[left][right], 
                            nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        return dp[0][-1]
