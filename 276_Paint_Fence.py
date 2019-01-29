class Solution:
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return k
        same, dif = k, k * (k - 1)
        for i in range(2, n):
            same, dif = dif, (same + dif) * (k - 1)
        return same + dif
