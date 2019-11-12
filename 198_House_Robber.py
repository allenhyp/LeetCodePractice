# Recursion (TLE)
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob(i):
            if i < 0: return 0
            return max(rob(i - 1), rob(i - 2), nums[i])
        return rob(len(nums) - 1)


# Recursion with memo
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n
        def rob(i):
            if i < 0: return 0
            if memo[i] >= 0: return memo[i]
            res = max(rob(i - 2) + nums[i], rob(i - 1))
            memo[i] = res
            return res
        return rob(n - 1)


# Iteration with memo
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        memo = [0] * (n + 1)
        memo[1] = nums[0]
        for i in range(1, n):
            memo[i + 1] = max(memo[i], memo[i - 1] + nums[i])
        return memo[-1]


# Iteration with O(1) space
class Solution:
    def rob(self, nums: List[int]) -> int:
        a = b = 0
        for n in nums:
            a, b = max(b + n, a), a
        return a
