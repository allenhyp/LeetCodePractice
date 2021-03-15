# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        slow = fast = head
        for _ in range(k - 1):
            fast = fast.next
        temp, fast = fast, fast.next
        while fast:
            slow, fast = slow.next, fast.next
        slow.val, temp.val = temp.val, slow.val
        return head
