class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # diff = S - 2*S2
        S, S2, n = sum(stones), 0, len(stones)
        dp = [[False] * (S + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True
            
        for i in range(1, n + 1):
            for s in range(1, S // 2 + 1):
                if dp[i - 1][s] or (s >= stones[i - 1] and dp[i - 1][s - stones[i - 1]]):
                    dp[i][s] += 1
                    S2 = max(S2, s)
        
        return S - 2 * S2
