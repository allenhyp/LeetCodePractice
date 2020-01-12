class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            a = str(i)
            b = str(n - i)
            if '0' not in a and '0' not in b:
                return [a, b]
