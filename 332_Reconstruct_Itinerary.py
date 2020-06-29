from collections import defaultdict
import heapq
class Solution:
    def dfs(self, dpt):
        while len(self.targets[dpt]):
            arv = heapq.heappop(self.targets[dpt])
            self.dfs(arv)
        self.res.append(dpt)
        
        
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.targets = defaultdict(list)
        self.res = []
        for dpt, arv in tickets:
            heapq.heappush(self.targets[dpt], arv)
        self.dfs('JFK')
        return self.res[::-1]
