class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n, mod = len(board), 10 ** 9 + 7
        dp = [[[float('-inf'), 0] for _ in range(n + 1)] for __ in range(n + 1)]
        dp[n - 1][n - 1] = [0, 1]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] in 'XS': continue
                for di, dj in [(1, 0), (0, 1), (1, 1)]:
                    if dp[i][j][0] < dp[i + di][j + dj][0]:
                        dp[i][j] = [dp[i + di][j + dj][0], 0]
                    if dp[i][j][0] == dp[i + di][j + dj][0]:
                        dp[i][j][1] += dp[i + di][j + dj][1]
                dp[i][j][0] += int(board[i][j]) if i or j else 0
        return [dp[0][0][0], dp[0][0][1] % mod] if dp[0][0][1] > 0 else [0, 0]
