class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                if (i - len(w) == -1 or dp[i - len(w)]) and w == s[i - len(w) + 1:i + 1]:
                    dp[i] = True
                    break
        return dp[-1]
