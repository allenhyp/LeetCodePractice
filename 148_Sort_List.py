# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeLists(self, l1, l2):
        dummy = ListNode(0)
        it = dummy
        while l1 and l2:
            if l1.val < l2.val:
                it.next = l1
                l1 = l1.next
            else:
                it.next = l2
                l2 = l2.next
            it = it.next
        if l1:
            it.next = l1
        if l2:
            it.next = l2
        return dummy.next
    
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return self.mergeLists(self.sortList(head), self.sortList(slow))
