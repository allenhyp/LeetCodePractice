class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n+1)
        for i in range(1, n+1):
            curMax = 0
            for j in range(1, min(k, i)+1):
                curMax = max(curMax, arr[i-j])
                dp[i] = max(dp[i], dp[i-j] + curMax*j)
                
        return dp[-1]
