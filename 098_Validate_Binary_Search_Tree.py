# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, min_node, max_node):
            if root is None:
                return True
            if (min_node and root.val <= min_node.val) or (max_node and root.val >= max_node.val):
                return False
            return helper(root.left, min_node, root) and helper(root.right, root, max_node)
        return helper(root, None, None)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inOrder(node, arr):
            if not node:
                return arr
            arr = inOrder(node.left, arr)
            arr.append(node.val)
            arr = inOrder(node.right, arr)
            return arr
        
        arr = inOrder(root, [])
        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1]:
                return False
        return True        
