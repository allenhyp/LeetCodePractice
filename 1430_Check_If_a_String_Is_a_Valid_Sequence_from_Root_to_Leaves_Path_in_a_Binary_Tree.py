# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        n = len(arr)
        def dfs(node, i):
            if node is None or node.val != arr[i]:
                return False
            if node.val == arr[i]:
                if i == n - 1:
                    return True if node.left is None and node.right is None else False
                else:
                    return dfs(node.left, i + 1) or dfs(node.right, i + 1)
        return dfs(root, 0)
