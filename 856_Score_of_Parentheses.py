class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack, cur = [], 0
        for p in S:
            if p == '(':
                stack.append(cur)
                cur = 0
            else:
                cur = stack.pop() + max(cur * 2, 1)
        return cur


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        level = res = 0
        for i in range(len(S)):
            level += 1 if S[i] == '(' else -1
            if S[i] == ')' and S[i - 1] == '(':
                res += 1 << level
        return res
