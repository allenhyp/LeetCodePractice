class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        pre = res = 0
        cur = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                res += min(pre, cur)
                pre = cur
                cur = 1
        
        return res + min(pre, cur)
