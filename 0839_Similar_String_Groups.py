class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv: return False
        if self.size[pu] < self.size[pv]:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv
        else:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        return True
        
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def similar(s1, s2):
            d = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    d += 1
            return d == 0 or d == 2

        n = len(strs)
        uf = UnionFind(n)
        groups = n
        for i in range(n):
            for j in range(i+1, n):
                if similar(strs[i], strs[j]) and uf.union(i, j):
                    groups -= 1
        return groups
