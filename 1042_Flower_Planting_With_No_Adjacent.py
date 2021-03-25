class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for x, y in paths:
            graph[x].append(y)
            graph[y].append(x)
        
        plantDict = {i: 0 for i in range(1, n + 1)}
        for cur in graph.keys():
            pick = set(range(1, 5))
            for adj in graph[cur]:
                if plantDict[adj] != 0 and plantDict[adj] in pick:
                    pick.remove(plantDict[adj])
            plantDict[cur] = pick.pop()
        return [plantDict[g] if plantDict[g] > 0 else 1 for g in range(1, n + 1)]
