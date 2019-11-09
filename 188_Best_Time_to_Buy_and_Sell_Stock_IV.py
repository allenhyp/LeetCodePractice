class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2: return 0
        if k >= n // 2:
            res = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    res += prices[i] - prices[i - 1]
            return res
        
        dp = [[0] * n for _ in range(k + 1)]
        for j in range(1, k + 1):
            minima = prices[0]
            for i in range(1, n):
                minima = min(minima, prices[i] - dp[j - 1][i - 1])
                dp[j][i] = max(dp[j][i - 1], prices[i] - minima)
        return dp[-1][-1]
