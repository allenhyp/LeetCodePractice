class Solution:
    def numSquares(self, n: 'int') -> 'int':
        dp = [0]
        sqrs = [x * x for x in range(1, int(math.sqrt(n)) + 1)]
        for i in range(1, n + 1):
            minimum = i
            for s in sqrs[:int(math.sqrt(i))]:
                minimum = min(minimum, dp[i - s] + 1)
            dp.append(minimum)
        return dp[-1]
