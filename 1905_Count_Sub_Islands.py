class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def floodfill(grid, m, n, r, c, num):
            if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                grid[r][c] = num
                for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    floodfill(grid, m, n, r+dr, c+dc, num)
        
        m2, n2 = len(grid2), len(grid2[0])
        num = 1
        for r in range(m2):
            for c in range(n2):
                if grid2[r][c] == 1:
                    num += 1
                    floodfill(grid2, m2, n2, r, c, num)

        check = set([i for i in range(2, num+1)])
        for r in range(m2):
            for c in range(n2):
                if grid2[r][c] > 1 and grid1[r][c] == 0:
                    check -= {grid2[r][c]}

        return len(check)
