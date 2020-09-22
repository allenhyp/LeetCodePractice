class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: (x[1], x[2]))
        cur = 0
        heap = []
        for trip in trips:
            while len(heap) > 0 and trip[1] >= heap[0][0]:
                cur -= heapq.heappop(heap)[2]
            cur += trip[0]
            heapq.heappush(heap, (trip[2], trip[1], trip[0]))
            if cur > capacity:
                return False
        return True
