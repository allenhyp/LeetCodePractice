# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.minimum, self.res = float('INF'), None
        def traverse(node):
            if node:
                if target == node.val:
                    self.res = node.val
                    return
                if abs(target - node.val) < self.minimum:
                    self.minimum = abs(target - node.val)
                    self.res = node.val
                traverse(node.left)
                traverse(node.right)
        traverse(root)
        return self.res
