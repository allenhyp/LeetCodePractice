class Solution:
    def check(self, nums: List[int]) -> bool:
        cap, last = nums[0], -inf
        rotate = False
        for num in nums:
            if num < last:
                if rotate: return False
                else: rotate = True
            else:
                if rotate and num > cap: return False
            last = num
        return True


class Solution:
    def check(self, nums: List[int]) -> bool:
        k, n = 0, len(nums)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]: k += 1
            if k > 1: return False
        return True