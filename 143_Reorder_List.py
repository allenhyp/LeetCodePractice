# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        tail = slow.next
        curr = tail.next
        slow.next = None
        tail.next = None
        while curr is not None:
            temp = curr
            curr = curr.next
            temp.next = tail
            tail = temp
        
        curr = head
        while curr is not None and tail is not None:
            temp = curr.next
            curr.next = tail
            curr = temp
            temp = tail.next
            tail.next = curr
            tail = temp
