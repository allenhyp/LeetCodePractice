class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        ret = i = maximum = 0
        for ability in sorted(worker):
            while i < len(jobs) and ability >= jobs[i][0]:
                maximum = max(maximum, jobs[i][1])
                i += 1
            ret += maximum
        return ret
