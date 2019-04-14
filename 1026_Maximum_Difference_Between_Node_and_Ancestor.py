# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def traverse(maximum, minimum, node):
            if not node:
                return 0
            cur = max(abs(node.val - maximum), abs(node.val - minimum))
            temp_max, temp_min = maximum, minimum
            maximum, minimum = max(node.val, maximum), min(node.val, minimum)
            return max(cur, traverse(maximum, minimum, node.left), traverse(maximum, minimum, node.right))
        if not root:
            return 0
        return max(traverse(root.val, root.val, root.left), traverse(root.val, root.val, root.right))
