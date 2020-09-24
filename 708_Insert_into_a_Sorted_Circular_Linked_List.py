"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head is None:
            head = Node(insertVal)
            head.next = head
            return head
        
        prev, curr = head, head.next
        while True:
            if ((prev.val <= insertVal and insertVal <= curr.val) or
                (prev.val > curr.val and insertVal < curr.val) or
                (prev.val > curr.val and insertVal > prev.val)):
                break
            prev, curr = prev.next, curr.next
            if prev == head: break
        prev.next = Node(insertVal, curr)
        return head
