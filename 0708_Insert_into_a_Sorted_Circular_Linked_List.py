"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            node = Node(val=insertVal)
            node.next = node
            return node
        
        node = head
        while node and node.next:
            if node.val <= insertVal <= node.next.val \
                or node.val > node.next.val and (insertVal >= node.val or insertVal <= node.next.val) \
                or node.next == head:
                break
            node = node.next

        newNode = Node(val=insertVal, next=node.next)
        node.next = newNode
        return head
