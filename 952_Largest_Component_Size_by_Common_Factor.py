class UF:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.size = [1] * N
        self.maximum = 1
    
    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if (rootX != rootY):
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]
            self.maximum = max(self.maximum, self.size[rootY])
    
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        N = len(A)
        uf = UF(N)
        dic = {}
        def factors(a):
            res = set()
            while a % 2 == 0:
                a //= 2
                res.add(2)
            for i in range(3, int(sqrt(a)) + 1, 2):
                while a % i == 0:
                    res.add(i)
                    a //= i
            if a > 2:
                res.add(a)
            return res
                
        for i in range(N):
            a = A[i]
            for factor in factors(a):
                if factor not in dic:
                    dic[factor] = i
                else:
                    uf.union(i, dic[factor])
        return uf.maximum
