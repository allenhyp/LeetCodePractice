class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        prefix, suffix = [1] * (size + 1) , [1] * (size + 1)
        for i, n in enumerate(nums):
            prefix[i + 1] = prefix[i] * n
        for i, n in reversed(list(enumerate(nums))):
            suffix[i] = suffix[i + 1] * n
        ret = [0] * size
        for i in range(size):
            ret[i] = prefix[i] * suffix[i + 1]
        return ret

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
