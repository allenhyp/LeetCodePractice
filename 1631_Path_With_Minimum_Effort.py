class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        heap = [(0, 0, 0)]
        dist = [[float('inf')] * n for _ in range(m)]
        directions = [0, 1, 0, -1, 0]
        while len(heap):
            d, r, c = heappop(heap)
            if d > dist[r][c]: continue
            if r == m - 1 and c == n - 1: return d
            for i in range(4):
                nr, nc = r + directions[i], c + directions[i + 1]
                if 0 <= nr < m and 0 <= nc < n:
                    nd = max(d, abs(heights[nr][nc] - heights[r][c]))
                    if nd < dist[nr][nc]:
                        dist[nr][nc] = nd
                        heappush(heap, (nd, nr, nc))
