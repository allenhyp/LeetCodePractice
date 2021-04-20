# Top-Down DP
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = [-1] * (target + 1)
        memo[0] = 1
        def helper(target):
            if memo[target] != -1:
                return memo[target]
            res = 0
            for num in nums:
                if target - num >= 0:
                    res += helper(target - num)
            memo[target] = res
            return res
        return helper(target)

# Bottom-Up DP
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = [0] * (target + 1)
        memo[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    memo[i] += memo[i - num]
        return memo[target]
