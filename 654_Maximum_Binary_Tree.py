# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) > 0:
            val = max(nums)
            root = TreeNode(val)
            idx = nums.index(val)
            root.left = self.constructMaximumBinaryTree(nums[:idx])
            root.right= self.constructMaximumBinaryTree(nums[idx+1:])
            return root
