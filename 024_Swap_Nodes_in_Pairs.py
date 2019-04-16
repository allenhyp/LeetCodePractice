# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head and head.next:
            temp = head.next
            prev.next = temp
            head.next = temp.next
            temp.next = head
            prev = head
            head = head.next
        return dummy.next
