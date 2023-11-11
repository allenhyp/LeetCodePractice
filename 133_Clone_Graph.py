"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def clone(self, node):
        if not node:
            return None
        if node in self.visited:
            return self.visited[node]

        curr = Node(node.val)
        self.visited[node] = curr
        for neighbor in node.neighbors:
            curr.neighbors.append(self.clone(neighbor))
        
        return curr

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.visited = {}
        return self.clone(node)
