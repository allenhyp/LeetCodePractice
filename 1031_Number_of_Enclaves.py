class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n:
                if A[i][j]:
                    A[i][j] = 0
                    dfs(i - 1, j)
                    dfs(i + 1, j)
                    dfs(i, j - 1)
                    dfs(i, j + 1)
        res = 0
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)
        for i in range(m):
            for j in range(n):
                if A[i][j]:
                    res += 1
        return res
