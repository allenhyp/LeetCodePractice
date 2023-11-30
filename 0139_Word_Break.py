# DFS with cache
class Solution:
    @cache
    def helper(self, s):
        ret = False
        for word in self.wordDict:
            if len(word) > len(s) or word != s[:len(word)]:
                continue
            if len(s) == len(word):
                return True
            else:
                ret |= self.helper(s[len(word):])
        return ret
                
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordDict = wordDict
        return self.helper(s)

# DP
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
