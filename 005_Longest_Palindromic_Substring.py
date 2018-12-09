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

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        n = len(s)
        dp = [[False for cols in range(n)] for rows in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1])
                if dp[i][j] and j - i + 1 > len(res):
                    res = s[i:j + 1]
        return res
