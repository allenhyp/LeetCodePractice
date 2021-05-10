class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        pq = [-t for t in target]
        heapq.heapify(pq)
        while True:
            a = -heapq.heappop(pq)
            total -= a
            if a == 1 or total == 1:
                return True
            if a < total or total == 0 or a % total == 0:
                return False
            a %= total
            total += a
            heapq.heappush(pq, -a)
