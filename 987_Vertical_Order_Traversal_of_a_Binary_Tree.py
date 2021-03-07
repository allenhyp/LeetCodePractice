# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        res, level, left, right = [[]], [(root, 0)], 0, 0
        while level:
            nxtl = []
            for node, idx in sorted(level, key=lambda x: x[0].val):
                if idx < left:
                    res.insert(0, [])
                    left -= 1
                elif idx > right:
                    res.append([])
                    right += 1
                res[idx - left].append(node.val)
                if node.left: nxtl.append((node.left, idx - 1))
                if node.right: nxtl.append((node.right, idx + 1))
            level = nxtl
        return res
