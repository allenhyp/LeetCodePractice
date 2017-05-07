class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        flag = 1
        if x < 0:
            flag = -1
            x = -x
        while x >= 1:
            result = result * 10 + x % 10
            x = x / 10
        return result * flag if -2147483648 <= result <= 2147483647 else 0
        