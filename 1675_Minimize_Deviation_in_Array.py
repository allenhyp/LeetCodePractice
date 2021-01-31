class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq = []
        res = minima = inf
        for num in nums:
            num = num * 2 if num % 2 else num
            heappush(pq, -num)
            minima = min(minima, num)

        while -pq[0] % 2 == 0:
            maxima = -heappop(pq)
            res = min(res, maxima - minima)
            minima = min(minima, maxima // 2)
            heappush(pq, -maxima // 2)
        
        return min(res, -pq[0] - minima)


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq = []
        for a in nums:
            heappush(pq, [a / (a & -a), a])
        res = float('inf')
        ma = max(a for a, a0 in pq)
        while len(pq) == len(nums):
            a, a0 = heappop(pq)
            res = min(res, ma - a)
            if a % 2 == 1 or a < a0:
                ma = max(ma, a * 2)
                heappush(pq, [a * 2, a0])
        return int(res)
