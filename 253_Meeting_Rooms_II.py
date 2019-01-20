# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        starts = []
        ends = []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        starts = sorted(starts)
        ends = sorted(ends)
        cur_earliest_end_int = 0
        total_req = 0
        for i in range(len(starts)):
            if starts[i] < ends[cur_earliest_end_int]:
                total_req += 1
            else:
                cur_earliest_end_int += 1
        return total_req

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals = sorted(intervals, key=lambda x: x.start)
        allocated = []
        for interval in intervals:
            if allocated and allocated[0] <= interval.start:
                heapq.heapreplace(allocated, interval.end)
            else:
                heapq.heappush(allocated, interval.end)
        return len(allocated)
