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


class Solution:
    def calculate(self, s: str) -> int:
        ret, _ = self.helper(s, 0)
        return ret

    def helper(self, s, i):
        curr = 0
        sign = 1
        temp = 0
        while i < len(s):
            if s[i].isdigit():
                temp = temp * 10 + int(s[i])
            else:
                if temp != 0:
                    curr += sign * temp
                    temp = 0

                if s[i] == '+':
                    sign = 1
                elif s[i] == '-':
                    sign = -1
                elif s[i] == '(':
                    temp, i = self.helper(s, i+1)
                elif s[i] == ')':
                    break
            i += 1
        return curr + sign * temp, i
