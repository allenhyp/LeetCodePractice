class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]


class Solution:
    def uniquePaths(self, m: 'int', n: 'int') -> 'int':
        res = 1.
        for i in range(1, m):
            res = res * (n - 1 + i) / i
        return int(res)
