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


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            left = right = i
            while left >= 0 and right < n and s[left] == s[right]:
                res, left, right = res + 1, left - 1, right + 1
            left, right = i - 1, i
            while left >= 0 and right < n and s[left] == s[right]:
                res, left, right = res + 1, left - 1, right + 1
        return res
