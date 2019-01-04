class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = set(J)
        res = 0
        for s in S:
            if s in jewels:
                res += 1
        return res
