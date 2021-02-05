class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cntr = collections.Counter(nums)
        res = 0
        for num in nums:
            if num + 1 in cntr:
                res = max(res, cntr[num + 1] + cntr[num])
        return res
