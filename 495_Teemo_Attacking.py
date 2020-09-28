class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if timeSeries == []: return 0
        res = 0
        for i in range(1, len(timeSeries)):
            res += min(timeSeries[i] - timeSeries[i - 1], duration)
        res += duration
        return res
