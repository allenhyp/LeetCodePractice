# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.min_dif, self.ret = float('inf'), root.val
        def traverse(node):
            if not node:
                return
            if node.val == target:
                self.min_dif = 0
                self.ret = node.val
                return
            
            if target < node.val:
                traverse(node.left)
            if abs(node.val - target) < self.min_dif:
                self.min_dif = abs(node.val - target)
                self.ret = node.val
            if target > node.val:
                traverse(node.right)

        traverse(root)
        return self.ret
