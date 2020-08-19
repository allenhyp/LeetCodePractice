class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return [i for i in range(10)]
        res = []
        
        def dfs(N, num):
            if N <= 0:
                res.append(num)
                return
            tail = num % 10
            nxt = set([tail + K, tail - K])
            for d in nxt:
                if 0 <= d < 10:
                    new_num = num * 10 + d
                    dfs(N - 1, new_num)
        
        for i in range(1, 10):
            dfs(N - 1, i)

        return res
