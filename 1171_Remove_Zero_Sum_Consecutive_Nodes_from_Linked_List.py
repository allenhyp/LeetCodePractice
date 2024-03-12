# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        acc = 0
        seen = {0: dummy}
        node = head
        while node:
            acc += node.val
            if acc in seen:
                prev = seen[acc]
                ref = prev
                aux = acc
                while prev != node:
                    prev = prev.next
                    aux += prev.val
                    if prev != node:
                        del seen[aux]
                ref.next = node.next
            else:
                seen[acc] = node
            node = node.next
        return dummy.next
