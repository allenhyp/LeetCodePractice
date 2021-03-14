class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        dp = {}
        mod = 10 ** 9 + 7
        arr.sort()
        for i in range(len(arr)):
            dp[arr[i]] = 1
            for j in range(0, i):
                dp[arr[i]] = (dp[arr[i]] + dp[arr[j]] * dp.get(arr[i] / arr[j], 0)) % mod
        return sum(dp.values()) % mod
