class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def getRealString(s):
            stack = []
            for c in s:
                if c != '#':
                    stack.append(c)
                elif len(stack):
                    stack.pop()
            return ''.join(stack)
        return getRealString(S) == getRealString(T)
