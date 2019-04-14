class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = collections.defaultdict(lambda: 1)
        for i in range(n):
            for j in range(i + 1, n):
                a, b = A[i], A[j]
                dp[b - a, j] = dp[b - a, i] + 1
        return max(dp.values())
