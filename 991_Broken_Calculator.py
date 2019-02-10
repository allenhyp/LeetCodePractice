class Solution:
    def brokenCalc(self, X: 'int', Y: 'int') -> 'int':
        res = 0
        while X < Y:
            Y = Y // 2 if Y % 2 == 0 else Y + 1
            res += 1
        return res + X - Y
