class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        dp = [[grid[0][0] for _ in range(m)] for __ in range(n)]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, m):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        prev = 0
        dp = []
        for item in grid[0]:
            cur = prev + item
            dp.append(cur)
            prev = cur
        for row in grid[1:]:
            for idx, item in enumerate(row):
                dp[idx] = min(dp[idx - 1], dp[idx]) + item
        return dp[-1]
