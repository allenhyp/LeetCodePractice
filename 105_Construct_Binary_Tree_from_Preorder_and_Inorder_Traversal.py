# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            ind =  inorder.index(preorder.pop(0))
            node = TreeNode(inorder[ind])
            node.left = self.buildTree(preorder, inorder[:ind])
            node.right = self.buildTree(preorder, inorder[ind + 1:])
            return node
        return None
