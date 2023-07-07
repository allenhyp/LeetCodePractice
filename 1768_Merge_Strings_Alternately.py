class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n, ret = len(word1), len(word2), ''
        if m == 0 and n == 0:
            return ret
        
        for i in range(min(m, n)):
            ret += word1[i] + word2[i]
        
        if m > n:
            ret += word1[n:]
        elif n > m:
            ret += word2[m:]
        
        return ret
