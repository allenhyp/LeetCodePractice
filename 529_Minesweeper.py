class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        r, c = click[0], click[1]
        if board[r][c] == 'M':
            board[r][c] = 'X'
        else:
            count = 0
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    i, j = r + dy, c + dx
                    if 0 <= i < m and 0 <= j < n and board[i][j] in ('M', 'X'):
                        count += 1
            if count == 0:
                board[r][c] = 'B'
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        if dx == 0 and dy == 0:
                            continue
                        i, j = r + dy, c + dx
                        if 0 <= i < m and 0 <= j < n and board[i][j] == 'E':
                            board = self.updateBoard(board, [i, j])
            else:
                board[r][c] = str(count)
        return board
