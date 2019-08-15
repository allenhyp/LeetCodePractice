class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = piles[:]
        for j in range(1, n):
            for i in range(n - j):
                dp[i] = max(piles[i] - dp[i + 1], piles[i + j] - dp[i])
        return dp[0] > 0
