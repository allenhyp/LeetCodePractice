class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for d in path.split('/'):
            if d == '..':
                if len(stack): stack.pop()
            elif d != '' and d != '.':
                stack.append(d)
        return '/' + '/'.join(stack)
