# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        thisNode = result
        while l1 and l2:
            if l1.val < l2.val:
                thisNode.next = l1
                l1 = l1.next
            else:
                thisNode.next = l2
                l2 = l2.next
            thisNode = thisNode.next
        thisNode.next = l1 if l1 else l2
        return result.next