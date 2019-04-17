# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        it, n = head, 1
        while it.next:
            it, n = it.next, n + 1
        tail, it = it, head
        tail.next = head
        for i in range(n - (k % n) - 1):
            it = it.next
        new_head, it.next = it.next, None
        return new_head
