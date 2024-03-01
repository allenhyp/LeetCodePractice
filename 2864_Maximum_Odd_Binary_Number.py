class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        if len(s) <= 1: return s
        cstr = [c for c in s]
        cstr.sort(reverse=True)
        return ''.join(cstr[1:] + cstr[:1])
