class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        result = {0: [[]], 1: [[s[0]]]}
        dp = [[False for _1_ in range(n)] for ___ in range(n)]
        for i in range(1, n):
            result[i + 1] = []
            for j in range(0, i + 1):
                if s[i] == s[j] and ((i - j <= 1) or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    ss = s[j : i + 1]
                    for prev in result[j]:
                        result[i + 1].append(prev + [ss])
        return result[n]
