class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n
        
        def checkFromV(v):
            color[v] = 0
            queue = [v]
            while queue:
                src = queue.pop(0)
                for dst in graph[src]:
                    if color[dst] == -1:
                        color[dst] = 1 - color[src]
                        queue.append(dst)
                    elif color[dst] == color[src]:
                        return False
            return True
        
        for i in range(n):
            if color[i] == -1 and not checkFromV(i):
                return False
        return True
