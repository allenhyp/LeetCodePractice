class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        s = s.lower()
        while left <= right:
            while left <= right and not s[left].isalnum():
                left += 1
            while left <= right and not s[right].isalnum():
                right -= 1
            if left <= right and s[left] != s[right]:
                return False
            left, right = left + 1, right - 1
        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = []
        for c in s.lower():
            if c.isalnum():
                clean.append(c)
        size = len(clean)
        return clean[:size//2] == clean[-1:(size-1)//2:-1]
