# DFS
from collections import defaultdict
class Solution:
    def hasNoCycle(self, v):
        self.visited[v] = True
        self.recStack[v] = True
        for u in self.prereqs[v]:
            if not self.visited[u]:
                if not self.hasNoCycle(u):
                    return False
            elif self.recStack[u]:
                return False
        self.recStack[v] = False
        return True
            
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.visited, self.recStack = {v: False for v in range(numCourses)}, {v: False for v in range(numCourses)}
        self.prereqs = defaultdict(list)
        for v, u in prerequisites:
            self.prereqs[u].append(v)
        
        for v in range(numCourses):
            if self.visited[v]:
                continue
            if not self.hasNoCycle(v):
                return False
        return True


# Topological sort (BFS)
class Solution:
    def buildGraph(self, n, pre):
        graph = [[] for _ in range(n)]
        for p in pre:
            graph[p[1]].append(p[0])
        return graph
    
    def computeIndegree(self, n, graph):
        degree = [0] * n
        for g in graph:
            for v in g:
                degree[v] += 1
        return degree
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.buildGraph(numCourses, prerequisites)
        degree = self.computeIndegree(numCourses, graph)
        for i in range(numCourses):
            target = 0
            while target < numCourses:
                if not degree[target]:
                    break
                target += 1
            if target == numCourses:
                return False
            degree[target] -= 1
            for p in graph[target]:
                degree[p] -= 1
        return True
