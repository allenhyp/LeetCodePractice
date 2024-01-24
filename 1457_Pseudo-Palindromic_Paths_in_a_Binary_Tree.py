# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def traverse(node, record):
            if not node:
                return 0
            
            record[node.val - 1] += 1
            if not node.left and not node.right:
                odd = 0
                for r in record:
                    odd += r % 2
                return 1 if odd <= 1 else 0
            return traverse(node.left, record.copy()) + traverse(node.right, record.copy())
        
        return traverse(root, [0 for i in range(9)])
