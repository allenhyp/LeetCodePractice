class Solution:
    def isHappy(self, n: int) -> bool:
        def happy(num):
            res = 0
            while num > 0:
                res += (num % 10) ** 2
                num //= 10
            return res
        
        visited = set()
        while n > 0:
            n = happy(n)
            if n == 1:
                return True
            elif n in visited:
                return False
            visited.add(n)
