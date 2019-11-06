# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root is None:
            return res
        stk = [root, root]
        while len(stk):
            cur = stk.pop()
            if len(stk) and cur == stk[-1]:
                if cur.right:
                    stk.extend([cur.right, cur.right])
                if cur.left:
                    stk.extend([cur.left, cur.left])
            else:
                res.append(cur.val)
        return res
