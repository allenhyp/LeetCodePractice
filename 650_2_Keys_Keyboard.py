class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0] * (n + 1);
        for k in range(2, n + 1):
            i = k >> 1
            while i >= 1 and k % i != 0:
                i -= 1
            dp[k] = dp[i] + k // i
        return dp[n]

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        for i in range(2, n + 1):
            if n % i == 0:
                return self.minSteps(n // i) + i
