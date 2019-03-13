class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        N = len(grid)
        memo = [[[None] * N for _1 in range(N)] for _2 in range(N)]
        def dp(r1, c1, c2):
            r2 = r1 + c1 - c2
            if r1 == N or c1 == N or r2 == N or c2 == N or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            elif r1 == N - 1 and c1 == N - 1:
                return grid[r1][c1]
            elif memo[r1][c1][c2] is not None:
                return memo[r1][c1][c2]
            else:
                ans = grid[r1][c1] + (c1 != c2) * grid[r2][c2]
                ans += max(dp(r1 + 1, c1, c2),
                           dp(r1 + 1, c1, c2 + 1),
                           dp(r1, c1 + 1, c2),
                           dp(r1, c1 + 1, c2 + 1))
                memo[r1][c1][c2] = ans
                return ans
        return max(0, dp(0, 0, 0))
