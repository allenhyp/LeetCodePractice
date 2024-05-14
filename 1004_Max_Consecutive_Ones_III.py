class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ret = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            while k < 0:
                k += 1 if nums[left] == 0 else 0
                left += 1
            ret = max(ret, right - left + 1)
        return ret
