from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # BFS
        m, n = len(mat), len(mat[0])
        q = deque([])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1
        
        while q:
            i, j = q.popleft()
            for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and mat[ni][nj] == -1:
                    mat[ni][nj] = mat[i][j] + 1
                    q.append((ni, nj))
        
        return mat


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # DP
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    continue
                up = inf if i == 0 else mat[i - 1][j]
                left = inf if j == 0 else mat[i][j - 1]
                mat[i][j] = min(up, left) + 1
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] == 0:
                    continue
                down = inf if i == m - 1 else mat[i + 1][j]
                right = inf if j == n - 1 else mat[i][j + 1]
                mat[i][j] = min(mat[i][j], down + 1, right + 1)
        
        return mat
