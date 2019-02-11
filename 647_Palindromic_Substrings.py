class Solution:
    def countSubstrings(self, s: 'str') -> 'int':
        n = len(s)
        dp = [[False for _ in range(n)] for __ in range(n)]
        res = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n, 1):
                dp[i][j] = (s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]))
                if dp[i][j]:
                    res += 1
        return res
