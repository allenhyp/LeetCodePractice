# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None or m == n:
            return head
        p = dummy = ListNode(0)
        dummy.next = head
        for _ in range(m - 1):
            p = p.next
        tail = p.next
        for _ in range(n - m):
            temp = p.next
            p.next = tail.next
            tail.next = tail.next.next
            p.next.next = temp
        return dummy.next
