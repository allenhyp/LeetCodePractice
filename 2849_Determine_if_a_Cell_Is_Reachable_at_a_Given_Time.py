class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        return abs(fx - sx) <= t and abs(fy - sy) <= t and not(fx == sx and fy == sy and t == 1)
