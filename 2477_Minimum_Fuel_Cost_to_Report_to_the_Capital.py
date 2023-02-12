from collections import defaultdict 
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        self.fuel = 0
        self.adj = defaultdict(list)
        for src, dst in roads:
            self.adj[src].append(dst)
            self.adj[dst].append(src)

        def dfs(current, parent):
            r = 1
            for child in self.adj[current]:
                if child != parent:
                    r += dfs(child, current)
            if current != 0:
                self.fuel += ceil(r / seats)
            return r
        
        dfs(0, -1)
                
        return self.fuel
