class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(d):
            temp = [0] * (target + 1)
            for j in range(1, f + 1):
                for k in range(j, target + 1):
                    temp[k] = (temp[k] + dp[k - j]) % 1000000007
            dp = temp
        return dp[-1]


from functools import lru_cache
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        @lru_cache(None)
        def dp(n, t):
            if n == 0 and t == 0:
                return 1
            elif n == 0 or t < 0:
                return 0
            res = 0
            for i in range(1, f + 1):
                res += dp(n - 1, t - i)
            return res
        return dp(d, target) % 1000000007
