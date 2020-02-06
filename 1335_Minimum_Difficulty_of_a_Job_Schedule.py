class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        dp = [[float('inf')] * n + [0] for _ in range(d + 1)]
        for d in range(1, d + 1):
            for i in range(n - d + 1):
                max_dif = 0
                for j in range(i, n - d + 1):
                    max_dif = max(max_dif, jobDifficulty[j])
                    dp[d][i] = min(dp[d][i], max_dif + dp[d - 1][j + 1])
        return dp[d][0] if dp[d][0] < float('inf') else -1
