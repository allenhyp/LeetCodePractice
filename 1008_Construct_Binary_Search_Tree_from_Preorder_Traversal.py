# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        self.index = 0
        self.size = len(preorder)
        def construct(minimum, maximum):
            if self.index >= self.size or not minimum < preorder[self.index] < maximum:
                return None
            key = preorder[self.index]
            root = TreeNode(key)
            self.index += 1
            root.left = construct(minimum, key)
            root.right = construct(key, maximum)
            return root
        return construct(float('-inf'), float('inf'))
