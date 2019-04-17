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
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = self.buildGraph(numCourses, prerequisites)
        degree = self.computeIndegree(numCourses, graph)
        res = []
        for i in range(numCourses):
            target = 0
            while target < numCourses:
                if not degree[target]:
                    break
                target += 1
            if target == numCourses:
                return []
            degree[target] -= 1
            res.append(target)
            for p in graph[target]:
                degree[p] -= 1
        return res
