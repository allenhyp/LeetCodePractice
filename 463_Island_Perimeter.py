class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.res = 0
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n:
                if grid[i][j] == 2: return 1
                elif grid[i][j] == 1:
                    grid[i][j] = 2
                    peri = (dfs(i - 1, j) +
                            dfs(i, j - 1) +
                            dfs(i, j + 1) +
                            dfs(i + 1, j))
                    self.res += 4 - peri
                    return 1
            return 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    dfs(i, j)
                    return self.res
        return 0

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    res += 4
                    if i > 0 and grid[i - 1][j]:
                        res -= 2
                    if j > 0 and grid[i][j - 1]:
                        res -= 2
        return res
