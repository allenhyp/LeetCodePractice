from collections import defaultdict
class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        row, col, diag, anti, ls = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int), set()
        for lamp in lamps:
            x, y = lamp[0], lamp[1]
            row[x] += 1
            col[y] += 1
            diag[x - y] += 1
            anti[x + y] += 1
            ls.add((x, y))
        res = []
        for i in range(len(queries)):
            x, y = queries[i][0], queries[i][1]
            if row[x] or col[y] or diag[x - y] or anti[x + y]:
                res.append(1)
            else:
                res.append(0)
            for r in range(x - 1, x + 2):
                for c in range(y - 1, y + 2):
                    if (r, c) in ls:
                        row[r] -= 1
                        col[c] -= 1
                        diag[r - c] -= 1
                        anti[r + c] -= 1
                        ls.remove((r, c))
        return res
