class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        r_i, r_j = -1, -1
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    r_i, r_j = i, j
                    break
        res = 0
        for i in range(r_i - 1, -1, -1):
            if board[i][r_j] == 'B':
                break
            elif board[i][r_j] == 'p':
                res += 1
                break
        for i in range(r_i + 1, 8):
            if board[i][r_j] == 'B':
                break
            elif board[i][r_j] == 'p':
                res += 1
                break
        for j in range(r_j - 1, -1, -1):
            if board[r_i][j] == 'B':
                break
            elif board[r_i][j] == 'p':
                res += 1
                break
        for j in range(r_j + 1, 8):
            if board[r_i][j] == 'B':
                break
            elif board[r_i][j] == 'p':
                res += 1
                break
        return res
