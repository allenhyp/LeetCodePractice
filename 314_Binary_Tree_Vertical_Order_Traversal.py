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

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        nodes = []
        def dfs(node, row, col):
            if node is not None:
                nodes.append((col, row, node.val))
                dfs(node.left, row + 1, col - 1)
                dfs(node.right, row + 1, col + 1)
        dfs(root, 0, 0)
        
        res = []
        nodes.sort()
        idx = nodes[0][0]
        cur = []
        for col, row, val in nodes:
            if col == idx:
                cur.append(val)
            else:
                res.append(cur)
                idx = col
                cur = [val]
        res.append(cur)
        return res
