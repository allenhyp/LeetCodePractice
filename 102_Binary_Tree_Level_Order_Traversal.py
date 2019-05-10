# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue, res = [root], []
        while queue:
            next, level = [], []
            for node in queue:
                level.append(node.val)
                if node.left is not None:
                    next.append(node.left)
                if node.right is not None:
                    next.append(node.right)
            res.append(level)
            queue = next
        return res
