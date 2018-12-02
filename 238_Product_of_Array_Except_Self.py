class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        n = len(nums)
        p = 1
        for i in range(1, n):
            res.append(p)
            p *= nums[i - 1]
        res.append(p)
        p = 1
        for i in range(n - 1, -1, -1):
            res[i] *= p
            p *= nums[i]
        return res
