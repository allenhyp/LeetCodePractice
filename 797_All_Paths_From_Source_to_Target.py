class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res, goal = [], len(graph) - 1
        def dfs(curr, path):
            if curr == goal:
                res.append(path)
            else:
                for i in graph[curr]:
                    dfs(i, path + [i])
        dfs(0, [0])
        return res
