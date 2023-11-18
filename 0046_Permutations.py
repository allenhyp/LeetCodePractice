class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def dfs(curr, remain):
            if len(remain) == 0:
                ret.append(curr.copy())
                return
            for i in range(len(remain)):
                curr.append(remain[i])
                dfs(curr, remain[:i] + remain[i+1:])
                curr.pop()
            return
        dfs([], nums)
        return ret
