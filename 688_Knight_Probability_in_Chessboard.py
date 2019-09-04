class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        memo = {}
        def helper(r, c, k):
            if 0 <= r <= N - 1 and 0 <= c <= N - 1:
                if k == 0:
                    return 1
                if (r, c, k) not in memo:
                    w = 0
                    for dr, dc in moves:
                        w += helper(r + dr, c + dc, k - 1)
                    memo[(r, c, k)] = memo.get((r, c, k), 0) + w
                return memo[(r, c, k)]
            return 0
        return helper(r, c, K) / 8 ** K
