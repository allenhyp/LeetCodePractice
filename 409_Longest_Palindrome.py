from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        gotOdd = False
        ret = 0
        for _, v in Counter(s).items():
            if v % 2 == 0:
                ret += v
            else:
                ret += v - 1
                if not gotOdd:
                    ret += 1
                    gotOdd = True
        
        return ret
