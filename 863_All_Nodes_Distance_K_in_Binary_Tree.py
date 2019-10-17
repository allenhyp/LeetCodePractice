# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        def dfs(child, parent=None):
            if child:
                child.parent = parent
                dfs(child.left, child)
                dfs(child.right, child)
        dfs(root)
        
        level = [target]
        seen = {target, None}
        for i in range(K):
            level = [nxt for node in level for nxt in (node.left, node.right, node.parent) if nxt not in seen]
            seen |= set(level)
        return [node.val for node in level]
