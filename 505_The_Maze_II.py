# BFS
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        if start[0] == destination[0] and start[1] == destination[1]:
            return 0
        queue = collections.deque()
        visited = [[False for _0 in range(n)] for _1 in range(m)]
        distances = [[float('inf') for _0 in range(n)] for _1 in range(m)]
        queue.append((start[0], start[1]))
        distances[start[0]][start[1]] = 0
        while len(queue):
            i, j = queue.popleft()
            if i != destination[0] or j != destination[1]:
                for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    ni, nj, dd = i + di, j + dj, 0
                    while 0 <= ni < m and 0 <= nj < n and maze[ni][nj] == 0:
                        ni, nj, dd = ni + di, nj + dj, dd + 1
                    if distances[i][j] + dd < distances[ni - di][nj - dj]:
                        distances[ni - di][nj - dj] = distances[i][j] + dd  
                        queue.append((ni - di, nj - dj))
        return -1 if distances[destination[0]][destination[1]] == float('inf') else distances[destination[0]][destination[1]]

# BFS with heapq
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n, pq, visited = len(maze), len(maze[0]), [(0, start[0], start[1])], {(start[0], start[1]): 0}
        while len(pq):
            d, i, j = heapq.heappop(pq)
            if i == destination[0] and j == destination[1]:
                return d
            for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                ni, nj, dd = i + di, j + dj, 0
                while 0 <= ni < m and 0 <= nj < n and maze[ni][nj] == 0:
                    ni, nj, dd = ni + di, nj + dj, dd + 1
                if (ni - di, nj - dj) not in visited or d + dd < visited[(ni - di, nj - dj)]:
                    visited[(ni - di, nj - dj)] = d + dd
                    heapq.heappush(pq, (d + dd, ni - di, nj - dj))
        return -1
