class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        hor, ver = [[0] * n for _ in range(m)], [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    hor[i][j] = 1 if j == 0 else hor[i][j - 1] + 1
                    ver[i][j] = 1 if i == 0 else ver[i - 1][j] + 1
        maximum = 0
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                small = min(hor[i][j], ver[i][j])
                while small > maximum:
                    if hor[i - small + 1][j] >= small and ver[i][j - small + 1] >= small:
                        maximum = small
                    small -= 1
        return maximum * maximum
