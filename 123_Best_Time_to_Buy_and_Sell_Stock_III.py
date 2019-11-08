class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        dp[k][i] = max(dp[k][i - 1], p[i] - p[j] + dp[k - 1][j - 1])
        '''
        
        n = len(prices)
        if n < 2: return 0
        dp = [[0] * n for _ in range(3)]
        for k in range(1, 3):
            minima = prices[0]
            for i in range(1, n):
                minima = min(minima, prices[i] - dp[k - 1][i - 1])
                dp[k][i] = max(dp[k][i - 1], prices[i] - minima)
        return dp[-1][-1]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        For each iteration, buy the share with the price as low as we can,
        and sell the share with the price as high as we can; then integrate
        the profit of the first trade into the cost of the second buy,
        eventually, the second sell would be the profit of the two transaction.
        '''
        
        buy1 = buy2 = float('inf')
        sell1 = sell2 = 0
        for p in prices:
            buy1 = min(buy1, p)
            sell1 = max(sell1, p - buy1)
            buy2 = min(buy2, p - sell1)
            sell2 = max(sell2, p - buy2)
        return sell2
