# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        dic = {}
        queue = [(root, 0)]
        for node, idx in queue:
            if node:
                if idx in dic.keys():
                    dic[idx].append(node.val)
                else:
                    dic[idx] = [node.val]
                queue += (node.left, idx - 1), (node.right, idx + 1)
        res = []
        for _, item in sorted(dic.items()):
            res.append(item)
        return res
