# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: 'TreeNode', x: 'int', y: 'int') -> 'bool':
        self.x_parent = self.y_parent = self.x_depth = self.y_depth = -1
        def traversal(root, depth, parent):
            if not root:
                return 0
            if root.val == x:
                self.x_parent = parent
                self.x_depth = depth
                print(x, depth)
            elif root.val == y:
                self.y_parent = parent
                self.y_depth = depth
                print(y, depth)
            if self.x_parent != -1 and self.y_parent != -1:
                if self.x_parent != self.y_parent and self.x_depth == self.y_depth:
                    return 1
                else:
                    return 0
            else:
                return max(traversal(root.right, depth + 1, root.val), traversal(root.left, depth + 1, root.val))
        return traversal(root, 0, root.val) == 1


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        level = [(root, None)]
        while len(level):
            next_level, found = [], []
            for node in level:
                if node[0].val in [x, y]:
                    found.append(node)
                if node[0].left is not None: next_level.append((node[0].left, node))
                if node[0].right is not None: next_level.append((node[0].right, node))
            if len(found) > 0:
                if len(found) == 2 and found[0][1] != found[1][1]:
                    return True
                return False
            level = next_level
        return False
