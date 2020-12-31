class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                cnt = 0
                for a in range(max(i - 1, 0), min(i + 2, m)):
                    for b in range(max(j - 1, 0), min(j + 2, n)):
                        cnt += board[a][b] & 1
                if cnt == 3 or (cnt - board[i][j] == 3):
                    board[i][j] |= 2
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
        return
