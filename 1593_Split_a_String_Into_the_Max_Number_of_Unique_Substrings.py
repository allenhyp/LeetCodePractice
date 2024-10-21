class Solution:
    def backtrack(self, s, i, used):
        if i >= len(s):
            return len(used)
        cur = ''
        maxima = 1
        while i < len(s):
            cur = cur + s[i]
            if cur not in used:
                used.add(cur)
                maxima = max(maxima, self.backtrack(s, i + 1, used))
                used.remove(cur)
            i += 1
        return maxima
    def maxUniqueSplit(self, s: str) -> int:
        return self.backtrack(s, 0, set())
