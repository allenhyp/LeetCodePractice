# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        left_stack = self.traverse(root1)
        right_stack = self.traverse(root2)
        res = []
        while len(left_stack) or len(right_stack):
            if (len(left_stack) == 0 or (len(right_stack) > 0 and 
                right_stack[-1].val <= left_stack[-1].val)):
                tmp = right_stack.pop()
                res.append(tmp.val)
                if tmp.right is not None:
                    right_stack.extend(self.traverse(tmp.right))
            else:
                tmp = left_stack.pop()
                res.append(tmp.val)
                if tmp.right is not None:
                    left_stack.extend(self.traverse(tmp.right))
        return res
        
    def traverse(self, root):
        stack = []
        while root is not None:
            stack.append(root)
            root = root.left
        return stack
