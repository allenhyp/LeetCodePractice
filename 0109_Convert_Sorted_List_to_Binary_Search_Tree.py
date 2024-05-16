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


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMid(self, head):
        slow = fast = head
        pre = slow
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        return pre, slow

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        pre, mid = self.findMid(head)
        root = TreeNode(mid.val)
        pre.next = None
        if mid != head:
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root
