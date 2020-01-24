# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def traverse(node, level):
            if node.left is None and node.right is None:
                return node.val, level
            (left_val, left_level) = traverse(node.left, level + 1) if node.left else (0, -1)
            (right_val, right_level) = traverse(node.right, level + 1) if node.right else (0, -1)
            if left_level > right_level:
                return left_val, left_level
            elif right_level > left_level:
                return right_val, right_level
            else:
                return left_val + right_val, left_level
        res, _ = traverse(root, 0)
        return res


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            cur_sum = 0
            for _ in range(size):
                node = queue.popleft()
                cur_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return cur_sum
