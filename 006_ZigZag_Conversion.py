class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2 or len(s) < 2:
            return s
        elif numRows == 2:
            return s[0::2] + s[1::2]

        a = ["" for i in range(numRows)]
        b = 2 * numRows - 2

        for i in xrange(len(s)):
            r = i % b
            if r < numRows:
                a[r] += s[i]
            else:
                a[2 * numRows - r - 2] += s[i]

        result = ""
        for i in range(numRows):
            result += a[i]
        return result
