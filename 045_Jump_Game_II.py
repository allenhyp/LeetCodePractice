class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        reach, jump, right_most = 0, 0, 0
        for i in range(len(nums) - 1):
            right_most = max(right_most, i + nums[i])
            if i == reach:
                jump += 1
                reach = right_most
        return jump
