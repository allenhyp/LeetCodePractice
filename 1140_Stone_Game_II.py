class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        acc = piles[:]
        for i in range(n - 2, -1, -1):
            acc[i] += acc[i + 1]
        
        from functools import lru_cache
        @lru_cache(None)
        
        def dp(index, m):
            max_val = 0
            for i in range(index, min(index + 2 * m, n)):
                next_m = max(m, i - index + 1)
                max_val = max(max_val, acc[index] - dp(i + 1, next_m))
            return max_val
        
        return dp(0, 1)
