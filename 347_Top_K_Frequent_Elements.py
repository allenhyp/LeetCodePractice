class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic, q, res = {}, [], []
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
        for key, val in dic.items():
            heapq.heappush(q, (-val, key))
        for i in range(k):
            res.append(heapq.heappop(q)[1])
        return res
