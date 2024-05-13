class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = collections.defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = {}
        def dfs(index, parent):
            ret = 0
            for next in adj[index]:
                if next != parent:
                    ret += dfs(next, index)
            if ret > 0 or hasApple[index]:
                return ret + 1
            else:
                return 0
        
        return max(2 * (dfs(0, -1) - 1), 0)
