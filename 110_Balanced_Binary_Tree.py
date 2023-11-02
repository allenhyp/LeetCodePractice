# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def traverse(node):
            if not node:
                return 0, True
            leftHeight, leftBalanced = traverse(node.left)
            rightHeight, rightBalanced = traverse(node.right)
            return max(leftHeight, rightHeight) + 1, abs(leftHeight - rightHeight) <= 1 and leftBalanced and rightBalanced
        _, b = traverse(root)
        return b


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(node):
            if node is None:
                return 0
            left = height(node.left)
            right = height(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        return height(root) != -1
