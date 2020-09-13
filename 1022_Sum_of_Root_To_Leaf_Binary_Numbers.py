# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def traverse(node, cur):
            cur = cur * 2 + node.val
            if node.left is None and node.right is None:
                return cur
            left = traverse(node.left, cur) if node.left else 0
            right = traverse(node.right, cur) if node.right else 0
            return left + right
        return traverse(root, 0)
