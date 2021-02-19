class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = list(s)
        indices = []
        for i, c in enumerate(res):
            if c == '(':
                indices.append(i)
            elif c == ')':
                if indices: indices.pop()
                else: res[i] = ''
        while indices:
            res[indices.pop()] = ''
        return "".join(res)
