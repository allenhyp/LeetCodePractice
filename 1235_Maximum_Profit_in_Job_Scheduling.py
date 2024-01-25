class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda t: t[1]) # sort by endTime
        ends = [0]
        profits = [0]
        for s, e, p in jobs:
            i = bisect.bisect_right(ends, s) - 1
            p = max(profits[-1], profits[i] + p)
            ends.append(e)
            profits.append(p)

        return profits[-1]
