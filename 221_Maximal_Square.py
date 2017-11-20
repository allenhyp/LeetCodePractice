class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        n = len(matrix)
        m = len(matrix[0])

        dp = [[0 for _1_ in range(m)] for ___ in range(n)]
        max_s = 0
        for i in range(0, n):
            for j in range(0, m):
                if i == 0 or j == 0:
                    dp[i][j] = (int(matrix[i][j]))
                elif matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1])) + 1
                max_s = max(max_s, dp[i][j])
        return max_s**2
        