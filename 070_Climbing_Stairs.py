class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        f0, f1 = 1, 1
        for i in range(2, n + 1):
            t = f1
            f1 = f0 + f1
            f0 = t
        return f1
