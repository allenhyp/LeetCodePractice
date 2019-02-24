# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        new_node = TreeNode(val)
        if not root or root.val < val:
            new_node.left = root
            return new_node
        node = root
        while node.val > val:
            if not node.right or node.right.val < val:
                new_node.left = node.right
                node.right = new_node
                return root
            node = node.right
        return root
