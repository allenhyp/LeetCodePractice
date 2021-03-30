class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        res = []
        i = j = 0
        for c in target:
            row, col = divmod(ord(c) - ord('a'), 5)
            di, dj = row - i, col - j
            res.extend(['L'] * -min(dj, 0))
            res.extend(['U'] * -min(di, 0))
            res.extend(['D'] * max(di, 0))
            res.extend(['R'] * max(dj, 0))
            res.append('!')
            i, j = row, col
        return ''.join(res)
