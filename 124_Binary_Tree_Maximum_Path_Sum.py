# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maximum = float('-inf')
        def helper(node):
            if node is None: return 0
            left = max(0, helper(node.left))
            right = max(0, helper(node.right))
            self.maximum = max(self.maximum, node.val + left + right)
            return max(left, right) + node.val
        helper(root)
        return self.maximum
