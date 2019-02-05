# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: 'int') -> 'List[TreeNode]':
        if n == 0:
            return []
        def helper(start, end):
            tree_list = []
            for i in range(start, end + 1):
                for left in helper(start, i - 1):
                    for right in helper(i + 1, end):
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        tree_list.append(root)
            return tree_list or [None]
        return helper(1, n)
