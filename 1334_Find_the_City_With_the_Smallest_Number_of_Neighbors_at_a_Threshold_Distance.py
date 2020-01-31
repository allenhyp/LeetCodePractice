class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        res = smallest = n
        for e1, e2, w in edges:
            dist[e1][e2] = dist[e2][e1] = w
        for i in range(n):
            dist[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(i):
                    dist[i][j] = dist[j][i] = min(dist[i][j], dist[i][k] + dist[k][j])
        for i in range(n):
            count = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    count += 1
            if 0 < count <= smallest:
                res, smallest = i, count
        return res
