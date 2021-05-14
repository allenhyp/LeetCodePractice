# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def traverse(node):
            if not node:
                return node, node
            
            head, tail = traverse(node.left)
            if head:
                tail.right = node.right
                node.right = head
            node.left = None
            if tail and tail.right:
                _, tail = traverse(tail.right)
            else:
                _, tail = traverse(node.right)
            return node, (tail if tail else node)
        traverse(root)
        return
