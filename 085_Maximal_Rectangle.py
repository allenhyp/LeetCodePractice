class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        max_area = 0
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            cur = 0
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                width = dp[i][j] = dp[i][j - 1] + 1 if j else 1
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    max_area = max(max_area, width * (i - k + 1))
        return max_area


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        max_area = 0
        h = [0] * (n + 1)
        for i in range(m):
            s = []
            for j in range(n + 1):
                if j < n :
                    if matrix[i][j] == '1': h[j] += 1
                    else: h[j] = 0
                while len(s) > 0 and h[s[-1]] >= h[j]:
                    top = s.pop()
                    max_area = max(max_area, h[top] * (j - s[-1] - 1 if len(s) > 0 else j))
                s.append(j)
        return max_area
