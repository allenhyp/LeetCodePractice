class UF:
    def __init__(self, n):
        self.parents = [i for i in range(n)]

    def union(self, x, y):
        self.parents[self.find(x)] = self.find(y)
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UF(len(edges) + 1)
        ret = edges[0]

        for a, b in edges:
            if uf.find(a) == uf.find(b):
                ret = [a, b]
            uf.union(a, b)
        return ret
