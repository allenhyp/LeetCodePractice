class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        while a or b or c:
            ba, bb, bc = a & 1, b & 1, c & 1
            if ba | bb != bc:
                res += abs(ba + bb - bc)
            a >>= 1
            b >>= 1
            c >>= 1
        return res
