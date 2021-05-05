# DP (O(n ^ 2))
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        dp = [startFuel] + [0] * n
        # dp[t] = the maximum distance with t times of refueling
        for i, station in enumerate(stations):
            for t in range(i, -1, -1):
                if dp[t] >= station[0]:
                    dp[t + 1] = max(dp[t + 1], dp[t] + station[1])
        for t in range(n + 1):
            if dp[t] >= target: return t
        return -1

# Priority queue (O(n log n))
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        cur = startFuel
        res = i = 0
        pq = []
        while cur < target:
            while i < len(stations) and cur >= stations[i][0]:
                heapq.heappush(pq, -stations[i][1])
                i += 1
            if not pq: return -1
            cur += -heapq.heappop(pq)
            res += 1
        return res
