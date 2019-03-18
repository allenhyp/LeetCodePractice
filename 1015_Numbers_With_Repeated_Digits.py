class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        digits = list(map(int, str(N + 1)))
        res, n = 0, len(digits)
        
        def perm(m, n):
            return 1 if n == 0 else perm(m, n - 1) * (m - n + 1)
        
        for  i in range(1, n):
            res += 9 * perm(9, i - 1)
        
        s = set()
        for i, x in enumerate(digits):
            for j in range(0 if i else 1, x):
                if j not in s:
                    res += perm(9 - i, n - i - 1)
            if x in s: break
            s.add(x)
        return N - res
