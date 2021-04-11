class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        maximum = 0
        memo = {}
        def dfs(i, j):
            nonlocal maximum
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i, j)] = 1
            for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    if matrix[ni][nj] > matrix[i][j]:
                        memo[(i, j)] = max(memo[(i, j)], 1 + dfs(ni, nj))
            maximum = max(maximum, memo[(i, j)])
            return memo[(i, j)]
                        
        for i in range(m):
            for j in range(n):
                dfs(i, j)
        return max(memo.values())
