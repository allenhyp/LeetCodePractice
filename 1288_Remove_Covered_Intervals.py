class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        res, lower_bound, upper_bound = 0, float('inf'), float('-inf')
        for low, high in intervals:
            if low < lower_bound or high > upper_bound:
                res += 1
            lower_bound = min(lower_bound, low)
            upper_bound = max(upper_bound, high)
        return res
