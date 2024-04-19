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

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def helper(node):
            head = tail = node
            if node.left:
                head, left_tail = helper(node.left)
                node.left = left_tail
                left_tail.right = node

            if node.right:
                right_head, tail = helper(node.right)
                node.right = right_head
                right_head.left = node
            
            head.left = tail
            tail.right = head
            return head, tail

        if not root:
            return root
        head, _ = helper(root)
        return head
