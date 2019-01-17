# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        si = sorted(intervals, key=lambda x: x.start)
        for t in range(0, len(si) - 1):
            if si[t].end > si[t + 1].start:
                return False
        return True
