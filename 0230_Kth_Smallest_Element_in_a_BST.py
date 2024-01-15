# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node, arr):
            if not node:
                return arr
            arr = inorder(node.left, arr)
            arr.append(node.val)
            arr = inorder(node.right, arr)
            return arr
        
        return inorder(root, [])[k - 1]


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.ret = -1
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.k -= 1
            if self.k == 0:
                self.ret = node.val
                return
            dfs(node.right)

        dfs(root)
        return self.ret
