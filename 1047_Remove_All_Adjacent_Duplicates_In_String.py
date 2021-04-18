class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['', 0]]
        for c in s:
            if stack[-1][0] != c:
                stack.append([c, 1])
            else:
                if stack[-1][1] == k - 1:
                    stack.pop()
                else:
                    stack[-1][1] += 1
        return ''.join([c * cnt for c, cnt in stack])
