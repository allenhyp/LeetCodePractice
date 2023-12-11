class Solution:
    def myAtoi(self, s: str) -> int:
        num, sign, trailing = 0, None, True
        for c in s:
            if c == ' ' and trailing:
                continue
            elif sign is None and trailing and c in '+-':
                trailing = False
                sign = c == '+'
            elif c.isnumeric():
                trailing = False
                num = num * 10 + int(c)
            else:
                break
        sign = True if sign is None else sign
        num = num if sign else -num
        if num > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif num < -2 ** 31:
            return -2 ** 31
        else:
            return num
