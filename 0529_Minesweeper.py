class Solution:
    def __init__(self):
        self.adj = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        def expand(board, r, c):
            if not (0 <= r < m and 0 <= c < n):
                return
            if board[r][c] == 'E':
                b = 0
                for dr, dc in self.adj:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    if board[nr][nc] == 'M':
                        b += 1
                if b > 0:
                    board[r][c] = f'{b}'
                else:
                    board[r][c] = 'B'
                    for dr, dc in self.adj:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n:
                            expand(board, nr, nc)
        
        cr, cc = click[0], click[1]
        if board[cr][cc] == 'M':
            board[cr][cc] = 'X'
            return board
        expand(board, cr, cc)
        return board
