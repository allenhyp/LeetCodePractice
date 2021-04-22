class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        dp = [-1] * n
        mod = 10 ** 9 + 7
        def dfs(i):
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            if dp[i] != -1:
                return dp[i]
            
            num = res = 0
            for j in range(i, n):
                num = num * 10 + ord(s[j]) - ord('0')
                if num > k:
                    break
                res = (res + dfs(j + 1)) % mod
            
            dp[i] = res
            return res
        
        return dfs(0)
