# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [], []
        t = root
        while len(stack) > 0 or t:
            if t:
                stack.append(t)
                t = t.left
            else:
                p = stack[-1]
                res.append(p.val)
                stack.pop()
                t = p.right
        return res
