class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right, res = 0, len(nums) - 1, [-1, -1]
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if len(nums) == 0 or nums[left] != target:
            return res
        res[0], right = left, len(nums) - 1
        while left < right:
            mid = (left + right) // 2 + 1
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        res[1] = right
        return res
