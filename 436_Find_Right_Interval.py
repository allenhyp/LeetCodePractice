class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dic = sorted([(interval[0], i) for i, interval in enumerate(intervals)])
        res = []
        for interval in intervals:
            idx = bisect.bisect_left(dic, (interval[1],))
            res.append(-1 if idx == len(dic) else dic[idx][1])
        return res
