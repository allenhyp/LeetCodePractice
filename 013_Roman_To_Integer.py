class Solution1(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookUpTable = {'I': 1,
                       'V': 5,
                       'X': 10,
                       'L': 50,
                       'C': 100,
                       'D': 500,
                       'M': 1000
                       }
        result = 0
        thisInput = lookUpTable[s[0]]
        for i in range(1, len(s)):
            nextInput = lookUpTable[s[i]]
            if thisInput < nextInput:
                result = result - thisInput
            else:
                result = result + thisInput
            thisInput = nextInput
        result = result + thisInput
        return result


class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = level = 0
        for c in s[::-1]:
            if dic[c] >= level:
                res += dic[c]
                level = dic[c]
            else:
                res -= dic[c]
        return res
