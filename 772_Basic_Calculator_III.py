class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s + '#'
        n = len(s)
        def helper(i):
            stack, num, sign = [], 0, '+'
            while i < n:
                if s[i].isspace():
                    i += 1
                    continue
                if s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                elif s[i] == '(':
                    num, i = helper(i + 1)
                else:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack.append(stack.pop() * num)
                    elif sign == '/':
                        stack.append(int(stack.pop() / num))
                    if s[i] == ')':
                        return sum(stack), i + 1
                    sign, num = s[i], 0
                    i += 1
            return sum(stack)
        return helper(0)
