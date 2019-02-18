class Solution:
    def __init__(self):
        self.dp = [1] * 59
        self.dp[2] = 2
        for i in range(3, 59):
            for j in range(2, i):
                self.dp[i] = max(self.dp[i], j * max((i - j), self.dp[i - j]))

    def integerBreak(self, n: 'int') -> 'int':
        if n <= 2: return 1
        return self.dp[n]
