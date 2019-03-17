class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0: return 1
        res, c = 0, 1
        while N > 0:
            res += 0 if (N & 1) else c
            N >>= 1
            c <<= 1
        return res
