# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        cur = root
        while cur is not None:
            if cur.left is None:
                res.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right is not None and pre.right != cur:
                    pre = pre.right
                if pre.right is None:
                    pre.right = cur
                    res.append(cur.val)
                    cur = cur.left
                else:
                    pre.right = None
                    cur = cur.right
        return res
