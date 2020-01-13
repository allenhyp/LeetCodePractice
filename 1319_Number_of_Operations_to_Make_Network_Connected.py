# Union-Find
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if n - 1 > len(connections):
            return -1
        parent = [i for i in range(n)]
        def findParent(i):
            while i != parent[i]:
                i = parent[i]
            return i
        
        for conn in connections:
            p1 = findParent(conn[0])
            p2 = findParent(conn[1])
            if p1 != p2:
                parent[p2] = p1
        
        component = 0
        for i in range(n):
            if parent[i] == i:
                component += 1
        return component - 1


# DFS
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if n - 1 > len(connections):
            return -1
        g = [set() for _ in range(n)]
        for conn in connections:
            c1, c2 = conn[0], conn[1]
            g[c1].add(c2)
            g[c2].add(c1)
        
        visited = [False] * n
        def dfs(i):
            if visited[i]:
                return 0
            visited[i] = True
            for c in g[i]:
                dfs(c)
            return 1
        
        return sum(dfs(i) for i in range(n)) - 1
