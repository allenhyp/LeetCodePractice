class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        non_zero = []
        for i, val in enumerate(nums):
            if val != 0:
                non_zero.append(i)
        i = 0
        for nz in non_zero:
            nums[i] = nums[nz]
            i += 1
        
        for j in range(i,len(nums)):
            nums[j] = 0

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return
