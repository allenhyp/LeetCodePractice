class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        cut = [i - 1 for i in range(n + 1)] # needed cut for the first k characters
        for i in range(n):
            for j in range(n):
                if i - j < 0 or i + j >= n or s[i - j] != s[i + j]:
                    break
                cut[i + j + 1] = min(cut[i + j + 1], 1 + cut[i - j])
            
            for j in range(1, n):
                if i - j + 1 < 0 or i + j >= n or s[i - j + 1] != s[i + j]:
                    break
                cut[i + j + 1] = min(cut[i + j + 1], 1 + cut[i - j + 1])
            
        return cut[-1]
