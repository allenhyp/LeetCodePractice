class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = res = 0
        sign = 1
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] in '+-':
                res += sign * num
                num = 0
                sign = 1 if s[i] == '+' else -1
            elif s[i] == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif s[i] == ')':
                res += sign * num
                num = 0
                res = res * stack.pop() + stack.pop()
        if num != 0:
            res += sign * num
        return res
