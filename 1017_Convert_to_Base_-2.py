class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0: return "0"
        res = ""
        while N != 0:
            N, remainder = divmod(N, -2)
            if remainder < 0:
                N, remainder = N + 1, remainder + 2
            res += str(remainder)
        return res[::-1]

class Solution:
    def baseNeg2(self, N: int) -> str:
        res = []
        while N:
            res.append(N & 1)
            N = -(N >> 1)
        return "".join(map(str, res[::-1] or [0]))
