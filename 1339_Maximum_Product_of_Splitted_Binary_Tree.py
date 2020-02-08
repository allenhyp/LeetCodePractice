# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        subsums = set()
        def dfs(node):
            if node is None: return 0
            else:
                subsum = node.val + dfs(node.left) + dfs(node.right)
                subsums.add(subsum)
                return subsum
        total = dfs(root)
        maximum = 0
        for subsum in subsums:
            maximum = max(maximum, subsum * (total - subsum))
        return maximum % (10 ** 9 + 7)
