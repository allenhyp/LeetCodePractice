class Solution:
    @cache
    def dfs(self, r, c, remain):
        if r < 0 or r >= self.m or c < 0 or c >= self.n or remain < 1:
            return 0
        
        ret = (1 if r == 0 else 0) + (1 if r == self.m-1 else 0) +\
            (1 if c == 0 else 0) + (1 if c == self.n-1 else 0)
        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            ret += self.dfs(r + dr, c + dc, remain-1)
        return ret % self.mod

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        self.m = m
        self.n = n
        self.mod = 10**9+7
        return self.dfs(startRow, startColumn, maxMove)
