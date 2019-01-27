class Solution:
    def countTriplets(self, A: 'List[int]') -> 'int':
        res, n = 0, len(A)
        dp = [-1] * (1 << 16)
        for i in range(n):
            for j in range(n):
                temp = A[i] & A[j]
                if dp[temp] == -1:
                    dp[temp] = 0
                    for k in range(n):
                        if temp & A[k] == 0:
                            dp[temp] += 1
                res += dp[temp]
        return res
