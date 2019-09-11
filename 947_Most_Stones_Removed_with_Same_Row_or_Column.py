class Solution:
    def find(self, i):
            if self.parent[i] == i:
                return i
            return self.find(self.parent[i])
        
    def union(self, i, j):
        pi = self.parent.setdefault(i, i)
        pj = self.parent.setdefault(j, j)
        self.parent[self.find(pj)] = self.find(pi)

    def removeStones(self, stones: List[List[int]]) -> int:
        self.parent = {}
        for i, j in stones:
            self.union(i, ~j)
        
        return len(stones) - len({self.find(x) for x in self.parent})
