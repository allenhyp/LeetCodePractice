from typing import List
from collections import Counter
import heapq
class Solution:
    def getMinimumFruits(self, fruits: List[int]) -> int:
        counter = Counter(fruits)
        pq = []
        for _, cnt in counter.items():
            heapq.heappush(pq, -cnt)
        while len(pq) > 1:
            larger = -heapq.heappop(pq)
            smaller = -heapq.heappop(pq)
            if larger - smaller > 0:
                heapq.heappush(pq, smaller - larger)
        return 0 if len(pq) == 0 else -pq[0]


s = Solution()
# fruits = [3, 3, 1, 1, 2]
# fruits = [1, 2, 5, 6]
fruits = [3,3,4,3,3]
print(s.getMinimumFruits(fruits))
