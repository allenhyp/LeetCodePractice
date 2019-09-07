class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        pos, dp = {}, [[0] * n for _ in range(n)]
        for i in range(n):
            pos[A[i]] = i
            for j in range(i, n):
                dp[i][j] = 2
        for j in range(2, n):
            for i in range(j - 1, 0, -1):
                prev = A[j] - A[i]
                if prev >= A[i]:
                    break
                elif prev in pos:
                    dp[i][j] = dp[pos[prev]][i] + 1
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if dp[i][j] > 2:
                    res = max(res, dp[i][j])
        return res
