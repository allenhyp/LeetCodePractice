# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ret = 0
        def traverse(node):
            if not node:
                return 0, 0
            leftCount, leftTotal = traverse(node.left)
            rightCount, rightTotal = traverse(node.right)
            count = leftCount + rightCount + 1
            total = leftTotal + rightTotal + node.val
            if node.val == total // count:
                self.ret += 1
            return count, total
        traverse(root)
        return self.ret
