class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        maxLen = 1
        head = 0
        for i in xrange(len(s)):
            if i - maxLen >= 1 and s[i-maxLen-1:i+1] == s[i-maxLen-1:i+1][::-1]:
                head = i - maxLen - 1
                maxLen += 2
                continue
            if i - maxLen >= 0 and s[i-maxLen:i+1] == s[i-maxLen:i+1][::-1]:
                head = i - maxLen
                maxLen += 1
        return s[head:head + maxLen]
