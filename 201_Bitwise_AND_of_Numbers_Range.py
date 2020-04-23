class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        trans = 0
        while n != m:
            m, n = m >> 1, n >> 1
            trans += 1
        return m << trans
