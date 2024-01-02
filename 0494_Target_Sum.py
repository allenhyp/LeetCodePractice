class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int: 
        def dfs(index, curr):
            if (index, curr) in self.memo:
                return self.memo[(index, curr)]
            if index < 0 and curr == target:
                return 1
            if index < 0:
                return 0
            
            positive = dfs(index - 1, curr + nums[index])
            negative = dfs(index - 1, curr - nums[index])
            self.memo[(index, curr)] = positive + negative
            return self.memo[(index, curr)]
        
        self.memo = {}
        return dfs(len(nums) - 1, 0)


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        total = sum(nums)
        if (S + total) % 2 or not -total <= S <= total:
            return 0
        target = (S + total) // 2
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] += dp[i - num]
        return dp[target]
