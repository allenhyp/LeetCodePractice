class Solution:
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        res, row_hit, col_hit = 0, 0, [0 for _ in range(m)]
        for i in range(n):
            for j in range(m):
                if not j or grid[i][j - 1] == 'W':
                    row_hit = 0
                    for k in range(j, m):
                        if grid[i][k] == 'W':
                            break
                        elif grid[i][k] == 'E':
                            row_hit += 1
                if not i or grid[i - 1][j] == 'W':
                    col_hit[j] = 0
                    for k in range(i, n):
                        if grid[k][j] == 'W':
                            break
                        elif grid[k][j] == 'E':
                            col_hit[j] += 1
                if grid[i][j] == '0':
                    res = max(res, row_hit + col_hit[j])
        return res
