class Solution:
    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':
        dp = [0] * 366
        for i in range(1, 366):
            if i not in days:
                dp[i] = dp[i - 1]
                continue
            min_cost = dp[i - 1] + costs[0]
            min_cost = min(min_cost, dp[max(i - 7, 0)] + costs[1])
            min_cost = min(min_cost, dp[max(i - 30, 0)] + costs[2])
            dp[i] = min_cost
        return dp[-1]
