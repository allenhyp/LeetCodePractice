class Solution:
    # dynamic programming
    def __init__(self):
        return


    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        dp = [[[]]] + [[] for __ in range(target)]
        for i in range(1, target + 1):
            for c in candidates:
                if c > i: break
                for temp in dp[i - c]:
                    if not temp or c >= temp[-1]:
                        dp[i].append(temp + [c])
        return dp[target]


class Solution:
    # DFS (Backtracking)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        def dfs(i, curr, total):
            if total == target:
                ret.append(curr.copy())
                return
            if total > target or i >= len(candidates):
                return
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            curr.pop()
            dfs(i + 1, curr, total)
            return
        dfs(0, [], 0)
        return ret

def __main__():
    mySolution = Solution()
    candidates = [2, 3, 5]
    target = 8
    print (mySolution.combinationSum(candidates, target))


if __name__ == '__main__':
    __main__()
