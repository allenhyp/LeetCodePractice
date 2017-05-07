class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        xStr = str(x)
        result = 0
        end = -1
        minus = False
        if xStr[0] == '-':
            end = 0
            minus = True

        for i in range(len(xStr) - 1, end, -1):
            result = result * 10
            result = result + int(xStr[i])

        if minus:
            result = - result
            if result < -2147483648:
                return 0
            else:
                return result
        else:
            if result > 2147483647:
                return 0
            else:
                return result
        