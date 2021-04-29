from heapq import heappush, heappop, heappushpop
from collections import defaultdict
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small, large = [], []
        lookup = defaultdict(int)
        res = []
        for i in range(k):
            heappush(small, -nums[i])
        for i in range(k // 2):
            heappush(large, -heappop(small))
        
        for i in range(k, len(nums)):
            print(small, large)
            
            if k % 2: res.append(-small[0])
            else: res.append((-small[0] + large[0]) / 2)
                
            print(res)
            m, n, balance = nums[i - k], nums[i], 0
            
            if m <= -small[0]:
                balance -= 1
                if m == -small[0]:
                    heappop(small)
                else:
                    lookup[m] += 1
            else:
                balance += 1
                if m == large[0]:
                    heappop(large)
                else:
                    lookup[m] += 1

            if small and n <= -small[0]:
                balance += 1
                heappush(small, -n)
            else:
                balance -= 1
                heappush(large, n)
            
            if balance > 0:
                heappush(small, -heappop(large))
            elif balance < 0:
                heappush(large, -heappop(small))
            
            while small and lookup[small[0]]:
                lookup[-heappop(small)] -= 1
            while large and lookup[large[0]]:
                lookup[heappop(large)] -= 1

        return res
