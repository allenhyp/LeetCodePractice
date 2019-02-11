class Solution:
    def numDistinct(self, s: 'str', t: 'str') -> 'int':
        n, m = len(s), len(t)
        dp = [[1 for _ in range(n + 1)]]
        for i in range(1, m + 1):
            dp.append([0])
            for j in range(1, n + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i].append(dp[i - 1][j - 1] + dp[i][j - 1])
                else:
                    dp[i].append(dp[i][j - 1])
        return dp[-1][-1]
