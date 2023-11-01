class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            i = (l + r) // 2
            num = nums[i]
            if num == target:
                return i
            if num < target:
                l = i + 1
            else:
                r = i
        return -1
