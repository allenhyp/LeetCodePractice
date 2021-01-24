from collections import Counter
class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        m, n = len(a), len(b)
        ca = Counter(a)
        cb = Counter(b)
        res = m + n - max((ca + cb).values()) # case 3
        acc_a = acc_b = 0
        for c in string.ascii_lowercase:
            if c > 'a':
                res = min(res, m - acc_a + acc_b) # case 1
                res = min(res, n - acc_b + acc_a) # case 2
            acc_a += ca[c]
            acc_b += cb[c]

        return res
