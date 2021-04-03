from collections import Counter
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        size = len(strs)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            cnt = Counter(s)
            c0, c1 = cnt['0'], cnt['1']
            for i in range(m, c0 - 1, -1):
                for j in range(n, c1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - c0][j - c1] + 1)
        return dp[-1][-1]
