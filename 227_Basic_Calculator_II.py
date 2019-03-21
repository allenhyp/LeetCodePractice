class Solution:
    def calculate(self, s: str) -> int:
        stack, num, sign = [], 0, '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if not s[i].isdigit() and not s[i].isspace() or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                sign, num = s[i], 0
        return sum(stack)


class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack, num, mul_or_div = [], -1, 0
        for c in s:
            if c.isdigit():
                num = (num if num != -1 else 0) * 10 + int(c)
            elif c != ' ':
                stack.append(num)
                num = -1
                if mul_or_div:
                    pos, pre = stack.pop(), stack.pop()
                    stack.append(pre * pos if mul_or_div == 1 else pre // pos)
                    mul_or_div = 0
                if c == '*':
                    mul_or_div = 1
                elif c == '/':
                    mul_or_div = 2
                else:
                    stack.append(1 if c == '+' else -1)
        if num != -1:
            if mul_or_div:
                pos, pre = num, stack.pop()
                stack.append(pre * pos if mul_or_div == 1 else pre // pos)
            else:
                stack.append(num)
        while len(stack) > 1:
            pos, op, pre = stack.pop(), stack.pop(), stack.pop()
            stack.append(op * pos + pre)
        return stack[0]

def main():
    solution = Solution()
    print(solution.calculate("6/2 - 4*5/2 + 7/ 2-5 -10*2"))

if __name__ == "__main__":
    main()
            


