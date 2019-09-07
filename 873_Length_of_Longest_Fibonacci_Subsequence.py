class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        dp = {}
        s = set(A)
        for j in range(len(A)):
            for i in range(j):
                prev = A[j] - A[i]
                if prev < A[i] and prev in s:
                    dp[A[i], A[j]] = dp.get((prev, A[i]), 2) + 1
        return max(dp.values() or [0])
