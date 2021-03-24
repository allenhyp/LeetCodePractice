class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        counter = collections.Counter()
        res = maxf = 0
        for i in range(n):
            counter[s[i]] += 1
            maxf = max(maxf, counter[s[i]])
            if res < maxf + k:
                res += 1
            else:
                counter[s[i - res]] -= 1
        return res
