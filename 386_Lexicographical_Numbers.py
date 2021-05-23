class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted([str(i) for i in range(1, n + 1)])

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def dfs(cur, res):
            if cur <= n:
                res.append(cur)
                for i in range(10):
                    if cur * 10 + i <= n:
                        dfs(cur * 10 + i, res)
        
        res = []
        for i in range(1, 10):
            dfs(i, res)
        return res
