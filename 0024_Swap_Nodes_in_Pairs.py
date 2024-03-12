# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        ref = dummy
        while ref.next and ref.next.next:
            a, b = ref.next, ref.next.next
            temp = b.next
            
            ref.next = b
            b.next = a
            a.next = temp
            
            ref = a
        return dummy.next
