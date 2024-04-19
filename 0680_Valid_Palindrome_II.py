class Solution:
    def validPalindrome(self, s: str) -> bool:
        buf = True
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                remove_right, remove_left = s[l:r], s[l+1:r+1]
                return remove_right == remove_right[::-1] or remove_left == remove_left[::-1]
            else:
                l, r = l+1, r-1
        return True
