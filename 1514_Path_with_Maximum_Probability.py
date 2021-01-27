class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        heap = [(-1, start)]
        prob = [0] * n
        visited = set()
        vd = collections.defaultdict(list)
        for i, e in enumerate(edges):
            vd[e[0]].append((e[1], i))
            vd[e[1]].append((e[0], i))
                    
        while heap:
            p, v = heappop(heap)
            visited.add(v)
            if v == end: return -p
            for nv, i in vd[v]:
                if nv not in visited:
                    np = -p * succProb[i]
                    if np > prob[nv]:
                        prob[nv] = np
                        heappush(heap, (-np, nv))
        return 0
