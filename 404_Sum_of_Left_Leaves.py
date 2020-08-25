# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None: return 0
        def traverse(node, isLeft):
            if node.left is None and node.right is None:
                return node.val if isLeft else 0
            left = traverse(node.left, True) if node.left else 0
            right = traverse(node.right, False) if node.right else 0
            return left + right
        return traverse(root, False)
