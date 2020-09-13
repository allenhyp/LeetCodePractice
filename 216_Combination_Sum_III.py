class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def dfs(target, i, cur):
            if len(cur) > k: return
            for j in range(i, 10):
                tmp = cur + [j]
                if j < target:
                    dfs(target - j, j + 1, tmp)
                elif j == target and len(tmp) == k:
                    res.append(tmp)
        dfs(n, 1, [])
        return res
