class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {len(s): ['']}
        def dfs(i):
            if i not in memo:
                memo[i] = [s[i : j] + (tail and ' ' + tail)
                           for j in range(i + 1, len(s) + 1)
                           if s[i : j] in wordDict
                           for tail in dfs(j)]
            return memo[i]
        return dfs(0)
