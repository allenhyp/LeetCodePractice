# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue, idx = [root], 0
        while queue[idx]:
            queue.append(queue[idx].left)
            queue.append(queue[idx].right)
            idx += 1
        return not any(queue[idx:])

# DFS
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        def dfs(node):
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            if ((left & (left + 1) == 0 and left / 2 <= right <= left) or
                right & (right + 1) == 0 and right <= left <= right * 2 + 1):
                return left + right + 1
            else:
                return -1
        return dfs(root) > 0
        