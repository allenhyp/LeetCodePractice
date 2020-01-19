# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root is None: return root
        dummy = TreeNode(0)
        dummy.left = root
        def helper(parent, node, leftOrRight):
            if node.left:
                helper(node, node.left, 'LEFT')
            if node.right:
                helper(node, node.right, 'RIGHT')
            isLeaf = node.left is None and node.right is None
            if isLeaf and node.val == target:
                if leftOrRight == 'LEFT':
                    parent.left = None
                else:
                    parent.right = None
            return isLeaf
        helper(dummy, root, 'LEFT')
        return dummy.left


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root is None: return root
        if root.left is not None:
            root.left = self.removeLeafNodes(root.left, target)
        if root.right is not None:
            root.right = self.removeLeafNodes(root.right, target)
        return None if root.left is None and root.right is None and root.val == target else root
        