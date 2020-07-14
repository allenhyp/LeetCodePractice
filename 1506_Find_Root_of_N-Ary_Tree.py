"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        if len(tree) == 0: return None
        total = 0
        for p in tree:
            total += p.val
            for c in p.children:
                total -= c.val
        for p in tree:
            if p.val == total:
                return p


class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        seen = set()
        for p in tree:
            for c in p.children:
                seen.add(c)
        for p in tree:
            if p not in seen:
                return p
