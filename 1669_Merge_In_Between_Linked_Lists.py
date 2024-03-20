# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        tail = list2
        while tail.next:
            tail = tail.next

        dummy = ListNode(val=-1, next=list1)
        curr = dummy
        count = 0
        while count < a:
            curr = curr.next
            count += 1
        
        temp = curr.next
        curr.next = list2
        curr = temp

        while count < b:
            curr = curr.next
            count += 1
        
        tail.next = curr.next
        return dummy.next
