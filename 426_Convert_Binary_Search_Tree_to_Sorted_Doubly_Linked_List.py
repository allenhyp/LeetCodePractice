"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        self.head = Node(0, None, None)
        self.tail = self.head
        def prefixTraversal(root):
            if not root:
                return
            prefixTraversal(root.left)
            self.tail.right = root
            root.left = self.tail
            self.tail = root
            prefixTraversal(root.right)
        prefixTraversal(root)
        self.tail.right = self.head.right
        self.head.right.left = self.tail
        return self.head.right
