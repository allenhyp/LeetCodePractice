class Solution:
    def arrangeCoins(self, n: int) -> int:
        def triArea(h):
            return ((h + 1) * h) // 2
        start, end = 0, n
        while start <= end:
            mid = (start + end) // 2
            midArea = triArea(mid)
            if midArea <= n and triArea(mid + 1) > n:
                return mid
            elif midArea > n:
                end = mid - 1
            else:
                start = mid + 1
