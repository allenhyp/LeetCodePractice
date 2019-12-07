"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        pre = root
        while pre is not None:
            cur = pre
            while cur is not None:
                if cur.left is not None:
                    cur.left.next = cur.right
                if cur.right is not None and cur.next is not None:
                    cur.right.next = cur.next.left
                cur = cur.next
            pre = pre.left
        return root
