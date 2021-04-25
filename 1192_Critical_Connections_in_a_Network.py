# Trajan's Algorithm (find critical connections)
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def dfs(rank, cur, pre):
            low[cur], res = rank, []
            for nxt in graph[cur]:
                if nxt == pre:
                    continue
                if not low[nxt]:
                    res += dfs(rank + 1, nxt, cur)
                low[cur] = min(low[cur], low[nxt])
                if low[nxt] > rank:
                    res.append([cur, nxt])
            return res
        
        graph = [[] for _ in range(n)]
        low = [0] * n
        
        for src, dst in connections:
            graph[src].append(dst)
            graph[dst].append(src)
        
        return dfs(1, 0, -1)
