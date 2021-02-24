# Binary search each time while inserting
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        pq, res = [], []
        def search(num):
            left, right, mid = 0, len(pq) - 1, 0
            while left <= right:
                mid = (left + right) // 2
                if num > pq[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        for num in nums[::-1]:
            idx = search(num)
            pq.insert(idx, num)
            res.append(idx)
        return res[::-1]

# Binary Indexed Tree
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        rank, N, res = {v: i + 1 for i, v in enumerate(sorted(nums))}, len(nums), []
        BITree = [0] * (N + 1)
        def update(i):
            while i <= N:
                BITree[i] += 1
                i += (i & -i)
        
        def getSum(i):
            s = 0
            while i:
                s += BITree[i]
                i -= (i & -i)
            return s
        
        for num in nums[::-1]:
            res.append(getSum(rank[num] - 1))
            update(rank[num])
        
        return res[::-1]

# Binary search after sort
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        res = []
        for i, num in enumerate(nums):
            idx = bisect_left(sorted_nums, num)
            res.append(idx)
            sorted_nums.pop(idx) # pop the visited ones
        return res
