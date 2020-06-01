class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = 0, n - 1
        while start < end:
            mid = (start + end) // 2
            halveIsEven = (end - mid) % 2 == 0
            if nums[mid] == nums[mid + 1]:
                if halveIsEven:
                    start = mid + 2
                else:
                    end = mid - 1
            elif nums[mid] == nums[mid - 1]:
                if halveIsEven:
                    end = mid - 2
                else:
                    start = mid + 1
            else:
                return nums[mid]
        return nums[start]
