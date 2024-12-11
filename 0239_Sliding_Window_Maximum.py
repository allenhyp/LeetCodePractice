import heapq
from collections import defaultdict

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        cur = [-num for num in nums[:k]]
        heapq.heapify(cur)
        ret = [-cur[0]]
        should_pop = defaultdict(int)
        for i in range(k, len(nums)):
            should_pop[-nums[i - k]] += 1
            while cur and should_pop[cur[0]] > 0:
                should_pop[cur[0]] -= 1
                heapq.heappop(cur)
            heapq.heappush(cur, -nums[i])
            ret.append(-cur[0])
        return ret


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ret = []
        for i, num in enumerate(nums):
            while dq and dq[-1] < num:
                dq.pop()
            dq.append(num)
            if i >= k and dq[0] == nums[i - k]:
                dq.popleft()
            if i >= k - 1:
                ret.append(dq[0])
        return ret
