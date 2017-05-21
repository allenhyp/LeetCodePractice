class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        h = {}
        longestLen = 0
        start = 0
        for i in range(0, len(s)):
            if s[i] in h:
                start = max(start, h[s[i]] + 1)
            h[s[i]] = i
            longestLen = max(longestLen, i - start + 1)
        return longestLen
