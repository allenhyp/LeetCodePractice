class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_row = [[0] * 9 for _ in range(9)]
        seen_col = [[0] * 9 for _ in range(9)]
        seen_block = [[0] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num = ord(board[i][j]) - ord('0') - 1
                if (num < 0): continue
                k = (i // 3) * 3 + (j // 3)
                if seen_row[i][num] or seen_col[j][num] or seen_block[k][num]:
                    return False
                seen_row[i][num] = seen_col[j][num] = seen_block[k][num] = 1
        return True
