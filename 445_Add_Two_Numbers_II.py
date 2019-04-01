# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getLen(self, head):
        size = 0
        while head:
            size += 1
            head = head.next
        return size
    
    def addToFront(self, head, val):
        node = ListNode(val)
        node.next = head
        return node

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1, n2, res = self.getLen(l1), self.getLen(l2), None
        while n1 or n2:
            sum = 0
            if (n1 >= n2):
                sum += l1.val
                l1 = l1.next
                n1 -= 1
            if (n1 < n2):
                sum += l2.val
                l2 = l2.next
                n2 -= 1
            res = self.addToFront(res, sum)
        cur, carry, res = res, 0, None
        while cur:
            sum = cur.val + carry
            res = self.addToFront(res, sum % 10)
            carry = sum // 10
            tmp = cur
            cur = cur.next
            del tmp
        if carry:
            res = self.addToFront(res, carry % 10)
        return res
