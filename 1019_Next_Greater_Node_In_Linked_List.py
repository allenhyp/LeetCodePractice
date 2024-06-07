# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        answer = []
        cur = 0
        node = head
        while node:
            answer.append(0)
            while stack and stack[-1][1] < node.val:
                idx, _ = stack.pop()
                answer[idx] = node.val
            stack.append((cur, node.val))
            node = node.next
            cur += 1
        return answer
