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


class Solution2(object):
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
        thisInput = 0
        for c in s[::1]:
            nextInput = lookUpTable[c]
            if thisInput < nextInput:
                result -= thisInput
            else:
                result += thisInput
            thisInput = nextInput
        result += nextInput
        return result
