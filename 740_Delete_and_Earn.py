class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = max(nums)
        values = [0] * (n + 1)
        for num in nums:
            values[num] += num
        take, skip = 0, 0
        for i in range(1, n + 1):
            take, skip = skip + values[i], max(take, skip)
        return max(take, skip)        
