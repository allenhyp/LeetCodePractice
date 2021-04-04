class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        maximum = 0
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)
        
        if not stack: return n
        else:
            a, b = n, 0
            while stack:
                b = stack.pop()
                maximum = max(maximum, a - b - 1)
                a = b
            maximum = max(maximum, a)
            
        return maximum
