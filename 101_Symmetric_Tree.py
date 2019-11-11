# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(left, right):
            if left is None or right is None:
                return left == right
            if left.val != right.val:
                return False
            return helper(left.left, right.right) and helper(left.right, right.left)
        return True if root is None else helper(root.left, root.right)

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        stack = [(root.left, root.right)]
        while len(stack):
            pair = stack.pop()
            left, right = pair[0], pair[1]
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            stack.extend([(left.left, right.right), (left.right, right.left)])
        return True
