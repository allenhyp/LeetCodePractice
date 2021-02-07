# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        queue = []
        res = []
        if root is not None: queue.append(root)
        while len(queue):
            nxt = []
            res.append(queue[-1].val)
            for node in queue:
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)
            queue = nxt
        return res
