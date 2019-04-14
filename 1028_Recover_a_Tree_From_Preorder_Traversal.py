# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        i = 0
        stack = []
        while i < len(S):
            level, value = 0, 0
            while i < len(S) and S[i] == '-':
                level += 1
                i += 1
            while i < len(S) and S[i].isdigit():
                value = 10 * value + int(S[i])
                i += 1
            while len(stack) > level:
                stack.pop()
            node = TreeNode(value)
            if stack and stack[-1].left is None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
