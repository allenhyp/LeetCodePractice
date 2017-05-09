class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tail = 1
        length = len(nums)
        if length < 2:
            return length
        for i in range(1, length):
            if nums[i] != nums[i-1]:
                nums[tail] = nums[i]
                tail += 1
        return tail
