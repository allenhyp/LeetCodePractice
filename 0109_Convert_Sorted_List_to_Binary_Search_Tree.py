# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getLen(self, head):
        size = 0
        while (head):
            size += 1
            head = head.next
        return size
    
    def generate(self, n):
        if n == 0:
            return None
        root = TreeNode(0)
        root.left = self.generate(n // 2)
        root.val = self.node.val
        self.node = self.node.next
        root.right = self.generate(n - (n // 2) - 1)
        return root

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        self.node = head
        return self.generate(self.getLen(head))
