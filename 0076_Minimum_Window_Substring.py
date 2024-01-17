class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needs = collections.Counter(t)
        missing = len(t)
        i = 0
        minimum = len(s) + 1
        ret = ""
        for j in range(len(s)):
            missing -= needs[s[j]] > 0
            needs[s[j]] -= 1

            while missing == 0:
                if j - i < minimum:
                    minimum, ret = j - i + 1, s[i:j + 1]
                needs[s[i]] += 1
                missing += needs[s[i]] > 0
                i += 1
            
        return ret
