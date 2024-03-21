# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Iterative
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = None
        while head is not None:
            temp = head.next
            head.next = curr
            curr = head
            head = temp
        return curr

# Recursive
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        nextNode = head.next
        root = self.reverseList(nextNode)
        nextNode.next = head
        head.next = None
        return root
