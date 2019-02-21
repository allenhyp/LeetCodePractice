class Solution:
    def getMoneyAmount(self, n: 'int') -> 'int':
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for left in range(n, 0, -1):
            for right in range(left + 1, n + 1):
                dp[left][right] = min(x + max(dp[left][x - 1], dp[x + 1][right]) for x in range(left, right))
        return dp[1][n]
