class Solution:
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


def __main__():
    mySolution = Solution()
    candidates = [2, 3, 5]
    target = 8
    print (mySolution.combinationSum(candidates, target))


if __name__ == '__main__':
    __main__()
