# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        memo = {}
        def robsub(root):
            if root is None:
                return 0
            if root in memo:
                return memo[root]
            now, left, right = root.val, root.left, root.right
            if left is not None:
                now += robsub(left.left) + robsub(left.right)
            if right is not None:
                now += robsub(right.left) + robsub(right.right)
            
            later = robsub(left) + robsub(right)
            res = max(now, later)
            memo[root] = res
            return res
        return robsub(root)
            

class Solution:
    def rob(self, root: TreeNode) -> int:
        def robsub(root):
            if root is None:
                return (0, 0)
            left, right = robsub(root.left), robsub(root.right)
            now = root.val + left[1] + right[1]
            later = max(left) + max(right)
            return (now, later)
        return max(robsub(root))
