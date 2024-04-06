class Solution:
    def myPow(self, x: float, n: int) -> float:
        pow = 1
        if n < 0:
            x = 1.0/x
        n = abs(n)
        
        while n > 0:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow
