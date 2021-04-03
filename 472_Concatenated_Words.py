class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        d = set(words)
        memo = {}
        res = []
        def dfs(word):
            if word in memo:
                return memo[word]
            for i in range(1, len(word)):
                prefix, suffix = word[:i], word[i:]
                if prefix in d and (suffix in d or dfs(suffix)):
                    memo[word] = True
                    return True
            memo[word] = False
            return False
        
        for word in words:
            if dfs(word):
                res.append(word)
        return res
