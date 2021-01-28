class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = []
        for i in range(n):
            c = min((k - (n - i - 1)), 26)
            k -= c
            res.append(chr(c + 96))
        return "".join(res[::-1])
