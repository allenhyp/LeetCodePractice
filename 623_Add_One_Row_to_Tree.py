# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            r = TreeNode(val=v, left=root)
            return r
        level = [root]
        depth = 1
        while level and depth < d - 1:
            queue = []
            for node in level:
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            level = queue
            depth += 1
        
        for node in level:
            node.left = TreeNode(val=v, left=node.left)
            node.right = TreeNode(val=v, right=node.right)
        return root
