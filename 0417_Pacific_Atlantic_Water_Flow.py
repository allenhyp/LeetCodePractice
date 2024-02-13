class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]: return []
        m, n = len(matrix), len(matrix[0])
        p_visited = [[False] * n for _ in range(m)]
        a_visited = [[False] * n for _ in range(m)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        result = []
        
        def dfs(i, j, visited):
            visited[i][j] = True
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (0 <= ni < m and 0 <= nj < n
                    and not visited[ni][nj] and matrix[ni][nj] >= matrix[i][j]):
                    dfs(ni, nj, visited)
        
        for i in range(m):
            dfs(i, 0, p_visited)
            dfs(i, n - 1, a_visited)
        for j in range(n):
            dfs(0, j, p_visited)
            dfs(m - 1, j, a_visited)
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    result.append([i, j])
        return result
