# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        res = []
        stack = [root]
        idx = 0
        while stack:
            node = stack.pop()
            if not node:
                continue
            if node.val != voyage[idx]:
                return [-1]
            idx += 1
            if node.right and node.right.val == voyage[idx]:
                if node.left: res.append(node.val)
                stack.extend([node.left, node.right])
            else:
                stack.extend([node.right, node.left])
        return res
