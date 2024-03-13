# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        def traverse(node, path, curr):
            if not node:
                return
            curr += node.val
            p = path.copy()
            p.append(node.val)
            if curr == targetSum and not node.left and not node.right:
                self.res.append(p)
            traverse(node.left, p, curr)
            traverse(node.right, p, curr)
            return
        traverse(root, [], 0)
        return self.res
