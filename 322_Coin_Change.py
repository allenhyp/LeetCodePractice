class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        k = len(coins)
        dp = []
        new = []
        for j in xrange(amount+1):
            new.append(j/coins[0] if j%coins[0]==0 else sys.maxint)
        dp.append(new)
        for i in xrange(1,k):
            new = []
            for j in xrange(amount+1):
                if j >= coins[i]:
                    new.append(min(dp[i-1][j], new[j-coins[i]] + 1))
                else:
                    new.append(dp[i-1][j])
            dp.append(new)
        return -1 if dp[k-1][amount] == sys.maxint else dp[k-1][amount]
