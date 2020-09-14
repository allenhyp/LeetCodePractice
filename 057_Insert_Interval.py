class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = 0
        while idx < len(intervals):
            if intervals[idx][1] < newInterval[0]:
                idx += 1
                continue
            elif intervals[idx][0] > newInterval[1]:
                intervals.insert(idx, newInterval)
                return intervals
            newInterval[0] = min(newInterval[0], intervals[idx][0])
            newInterval[1] = max(newInterval[1], intervals[idx][1])
            intervals.pop(idx)
        return intervals + [newInterval]
