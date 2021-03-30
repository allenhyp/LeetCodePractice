# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less, greater = ListNode(), ListNode()
        cur, l, g = head, less, greater
        while cur:
            if cur.val < x:
                l.next = cur
                l = l.next
            else:
                g.next = cur
                g = g.next
            cur = cur.next
        g.next = None
        l.next = greater.next
        return less.next
