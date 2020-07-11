"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def dfs(node):
            if node is None: return node
            if node.child is None:
                if node.next is None: return node
                else: return dfs(node.next)
            else:
                temp = node.next
                tail = dfs(node.child)
                node.next = node.child
                node.next.prev = node
                node.child = None
                if temp is not None:
                    temp.prev = tail
                    tail.next = temp
                    return dfs(temp)
                return tail
                
        dfs(head)
        return head
