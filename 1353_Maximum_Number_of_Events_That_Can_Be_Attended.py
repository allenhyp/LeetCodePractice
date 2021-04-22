class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])
        n = len(events)
        pq = []
        res = day = idx = 0
        while idx < n or pq:
            if not pq:
                day = events[idx][0]
            while idx < n and day >= events[idx][0]:
                heapq.heappush(pq, events[idx][1])
                idx += 1
            heapq.heappop(pq)
            day += 1
            res += 1
            while pq and day > pq[0]:
                heapq.heappop(pq)
        return res
