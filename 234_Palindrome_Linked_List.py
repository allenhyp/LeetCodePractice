# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        rev = None
        while slow:
            temp = slow.next
            slow.next = rev
            rev = slow
            slow = temp
        
        slow = head
        while rev:
            if rev.val != slow.val:
                return False
            rev, slow = rev.next, slow.next
            
        return True
