class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(grid, r, c, num):
            res = 0
            if not (0 <= r < m and 0 <= c < n):
                return res
            if grid[r][c] != 1:
                return res
            grid[r][c] = num
            for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                res += dfs(grid, r+dr, c+dc, num)
            return res + 1

        def checkConnectedSize(grid, r, c, sizes):
            size = 1
            visited = set()
            for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nr, nc = r+dr, c+dc
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if grid[nr][nc] > 0 and grid[nr][nc] not in visited:
                    size += sizes[grid[nr][nc]]
                    visited.add(grid[nr][nc])
            return size

        num = 1
        sizes = {0: 0}
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    num += 1
                    sizes[num] = dfs(grid, r, c, num)
        
        maximum = max(sizes.values())
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    maximum = max(maximum, checkConnectedSize(grid, r, c, sizes))
        
        return maximum
