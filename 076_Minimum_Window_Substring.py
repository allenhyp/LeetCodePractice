class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, miss = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            miss -= need[c] > 0
            need[c] -= 1
            if miss <= 0:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if J == 0 or j - i < J - I:
                    I, J = i, j
        return s[I : J]
