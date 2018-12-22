# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def split(self, lists, idx, sz):
        if sz <= 1: return lists[idx]
        l = self.split(lists, idx, sz // 2)
        r = self.split(lists, idx + sz // 2, sz - sz // 2)
        return self.merge(l, r)

    
    def merge(self, l, r):
        dummy = ListNode(0)
        head = dummy
        while l and r:
            if l.val < r.val:
                head.next = l
                head = l
                l = l.next
            else:
                head.next = r
                head = r
                r = r.next
        if l:
            head.next = l
        if r:
            head.next = r
        return dummy.next
    
    
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        return self.split(lists, 0, len(lists))
        