class Solution:
    def orangesRotting(self, grid: 'List[List[int]]') -> 'int':
        m, n = len(grid), len(grid[0])
        def infection(grid, i, j, time):
            if 0 <= i < m and 0 <= j < n:
                if grid[i][j] == 1:
                    grid[i][j] = time
                    infection(grid, i - 1, j, time - 1)
                    infection(grid, i + 1, j, time - 1)
                    infection(grid, i, j - 1, time - 1)
                    infection(grid, i, j + 1, time - 1)
                elif grid[i][j] < 0:
                    if time > grid[i][j]:
                        grid[i][j] = time
                        infection(grid, i - 1, j, time - 1)
                        infection(grid, i + 1, j, time - 1)
                        infection(grid, i, j - 1, time - 1)
                        infection(grid, i, j + 1, time - 1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    infection(grid, i - 1, j, -1)
                    infection(grid, i + 1, j, -1)
                    infection(grid, i, j - 1, -1)
                    infection(grid, i, j + 1, -1)
        maxtime = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
                elif grid[i][j] < 0:
                    if maxtime > grid[i][j]:
                        maxtime = grid[i][j]
        return -maxtime
                