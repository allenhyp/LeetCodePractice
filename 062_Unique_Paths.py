class Solution:
    def uniquePaths(self, m: 'int', n: 'int') -> 'int':
        res = 1.
        for i in range(1, m):
            res = res * (n - 1 + i) / i
        return int(res)
