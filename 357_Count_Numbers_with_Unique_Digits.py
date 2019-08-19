class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        res, base = 10, 9
        for i in range(2, n + 1):
            base = base * (9 - i + 2)
            res += base
        return res
