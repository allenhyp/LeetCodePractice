# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cntA = cntB = 0
        itrA, itrB = headA, headB
        while itrA or itrB:
            if itrA:
                cntA += 1
                itrA = itrA.next
            if itrB:
                cntB += 1
                itrB = itrB.next
        
        large, small = max(cntA, cntB), 0
        if large == cntA:
            itrL, itrS, small = headA, headB, cntB
        else:
            itrL, itrS, small = headB, headA, cntA
        for i in range(large - small):
            itrL = itrL.next
        while itrL and itrS:
            if itrL == itrS:
                return itrL
            itrL = itrL.next
            itrS = itrS.next
        return None
