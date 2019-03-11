class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        s0, s1 = 0, -prices[0]
        for i in range(1, len(prices)):
            s0, s1 = max(s0, prices[i] + s1 - fee), max(s1, s0 - prices[i])
        return s0
