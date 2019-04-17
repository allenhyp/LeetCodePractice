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
