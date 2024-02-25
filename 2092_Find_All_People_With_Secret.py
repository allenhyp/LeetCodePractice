from collections import defaultdict

# BFS
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        known = set([0, firstPerson])
        
        groupedMeetings = []
        meetings.sort(key=lambda x:x[2])

        seenTime = set()
        
        for meeting in meetings:
            if meeting[2] not in seenTime:
                seenTime.add(meeting[2])
                groupedMeetings.append([])
            groupedMeetings[-1].append((meeting[0], meeting[1]))

        for groups in groupedMeetings:
            knows = set()
            graph = defaultdict(list)
            
            for x, y in groups:
                graph[x].append(y)
                graph[y].append(x)
                if x in known:
                    knows.add(x)
                if y in known:
                    knows.add(y)
                    
            queue = deque((knows))
        
            while queue:
                curr = queue.popleft()
                known.add(curr)
                for adj in graph[curr]:
                    if adj not in known:
                        known.add(adj)
                        queue.append(adj)

        return list(known)

# Union Find (with reset)
class UnionFind:
    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.rank = [1] * n
    
    def find(self, x) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y) -> bool:
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty:
            return False
        
        if (self.rank[rootx] > self.rank[rooty]):
            rootx, rooty = rooty, rootx
        self.parent[rootx] = rooty
        self.rank[rooty] += self.rank[rootx]
        return True

    def connected(self, x, y) -> bool:
        return self.find(x) == self.find(y)

    def reset(self, x) -> None:
        self.parent[x] = x

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        uf = UnionFind(n)
        uf.union(0, firstPerson)
        meetings.sort(key=lambda x: x[2])
        index = 0
        while index < len(meetings):
            time = meetings[index][2]
            pool = set()
            while index < len(meetings) and time == meetings[index][2]:
                x, y, _ = meetings[index]
                uf.union(x, y)
                pool.add(x)
                pool.add(y)
                index += 1
            for p in pool:
                if not uf.connected(p, 0):
                    uf.reset(p)
        
        return [x for x in range(n) if uf.connected(x, 0)]

