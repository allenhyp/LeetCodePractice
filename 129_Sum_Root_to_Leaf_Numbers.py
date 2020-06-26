# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def traverse(cur, node):
            if node is None: return 0
            cur = cur * 10 + node.val
            if node.left is None and node.right is None:
                return cur
            return traverse(cur, node.left) + traverse(cur, node.right)
        return traverse(0, root)
