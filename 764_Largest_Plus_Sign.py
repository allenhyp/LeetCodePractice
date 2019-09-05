class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        grid = [[N] * N for _ in range(N)]
        for mine_x, mine_y in mines:
            grid[mine_x][mine_y] = 0
        
        for i in range(N):
            l = r = u = d = 0
            for j, k in zip(range(N), reversed(range(N))):
                l = 0 if grid[i][j] == 0 else l + 1
                grid[i][j] = min(grid[i][j], l)
                
                r = 0 if grid[i][k] == 0 else r + 1
                grid[i][k] = min(grid[i][k], r)
                
                u = 0 if grid[j][i] == 0 else u + 1
                grid[j][i] = min(grid[j][i], u)
                
                d = 0 if grid[k][i] == 0 else d + 1
                grid[k][i] = min(grid[k][i], d)
        
        res = 0
        for i in range(N):
            for j in range(N):
                res = max(res, grid[i][j]) 
        return res
