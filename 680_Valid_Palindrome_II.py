class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                A, B = s[i + 1 : j + 1], s[i : j]
                return A == A[::-1] or B == B[::-1]
            i, j = i + 1, j - 1
        return True
