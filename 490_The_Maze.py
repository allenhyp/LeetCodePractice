class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        visited = [[False for _0 in range(n)] for _1 in range(m)]
        queue = collections.deque()
        queue.append((start[0], start[1]))
        visited[start[0]][start[1]] = True
        while len(queue):
            i, j = queue.popleft()
            if i == destination[0] and j == destination[1]:
                return True
            for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                ni, nj = i + di, j + dj
                while 0 <= ni < m and 0 <= nj < n and maze[ni][nj] == 0:
                    ni, nj = ni + di, nj + dj
                if not visited[ni - di][nj - dj]:
                    visited[ni - di][nj - dj] = True
                    queue.append((ni - di, nj - dj))
        return False
