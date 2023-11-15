class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh, curr = set(), set()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh.add((r, c))
                elif grid[r][c] == 2:
                    curr.add((r, c))
        
        count = 0
        while True:
            next = set()
            for r, c in curr:
                for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) in fresh:
                        fresh.remove((nr, nc))
                        next.add((nr, nc))
            if len(next) == 0:
                break
            count += 1
            curr = next
        return count if len(fresh) == 0 else -1


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
                