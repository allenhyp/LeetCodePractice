class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                p = i
                pv = nums[i]
                break
        else:
            nums = nums.reverse()
            return
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > pv:
                nums[i], nums[p] = nums[p], nums[i]
                l, r = p + 1, len(nums) - 1
                while l < r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
                return
