# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = fast = slow = ListNode(next=head)
        for _ in range(n):
            fast = fast.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return dummy.next
