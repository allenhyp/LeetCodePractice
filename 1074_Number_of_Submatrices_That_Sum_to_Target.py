class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for row in matrix:
            for i in range(1, n):
                row[i] += row[i - 1]
        res = 0
        for i in range(n):
            for j in range(i, n):
                memo = collections.defaultdict(int)
                cur, memo[0] = 0, 1
                for k in range(m):
                    cur += matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0)
                    res += memo[cur - target]
                    memo[cur] += 1
        return res
