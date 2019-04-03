class Solution:
    def compress(self, chars: List[str]) -> int:
        left, i = 0, 0
        while i < len(chars):
            c, length = chars[i], 1
            while i + 1 < len(chars) and c == chars[i + 1]:
                length, i = length + 1, i + 1
            chars[left] = c
            if length > 1:
                ls = str(length)
                chars[left + 1 : left + len(ls) + 1] = ls
                left += len(ls)
            left, i = left + 1, i + 1
        return left
