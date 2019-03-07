# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def traverse(parent, node):
            if not node:
                return False
            node.val += parent
            if node.left or node.right:
                return traverse(node.val, node.left) or traverse(node.val, node.right)
            else:
                return node.val == sum
        return traverse(0, root)
