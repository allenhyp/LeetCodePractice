# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maximum = 0
        def traverse(root):
            if root is None:
                return 0
            left = traverse(root.left)
            right = traverse(root.right)
            self.maximum = max(self.maximum, left + right)
            return max(left, right) + 1
        traverse(root)
        return self.maximum
