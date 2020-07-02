# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        self.res = []
        def traverse(node, level):
            if node is None: return
            if len(self.res) < level:
                self.res.append([node.val])
            else:
                self.res[level - 1].append(node.val)
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)
        traverse(root, 1)
        return self.res[::-1]
