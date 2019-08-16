class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        n = len(A)
        for i in range(1, n):
            for j in range(0, n):
                A[i][j] += min(A[i - 1][j], A[i - 1][max(0, j - 1)], A[i - 1][min(n - 1, j + 1)])
        return min(A[-1])
