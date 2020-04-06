class Solution:
    def longestDiverseString(self, a: int, b: int, c: int, aa='a', bb='b', cc="c") -> str:
        if a < b:
            return self.longestDiverseString(b, a, c, bb, aa, cc)
        elif b < c:
            return self.longestDiverseString(a, c, b, aa, cc, bb)
        elif b == 0:
            return aa * min(a, 2)
        use_a = min(a, 2)
        use_b = 1 if (a - use_a >= b) else 0
        return aa * use_a + bb * use_b + self.longestDiverseString(a - use_a, b - use_b, c, aa, bb, cc)
