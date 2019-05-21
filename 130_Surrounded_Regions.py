class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return
        m, n = len(board), len(board[0])
        def dfs(board, i, j):
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'N'
                for di, dj in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
                    board = dfs(board, i + di, j + dj)
            return board
                        
        for i in (0, m - 1):
            for j in range(n):
                board = dfs(board, i, j)
        for j in (0, n - 1):
            for i in range(m):
                board = dfs(board, i, j)
        
        for i in range(m):
            for j in range(n):
                board[i][j] = 'O' if board[i][j] == 'N' else 'X'
