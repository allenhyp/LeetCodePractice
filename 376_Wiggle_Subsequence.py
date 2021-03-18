class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        last, res = 0, 1
        for i in range(1, len(nums)):
            curr = nums[i] - nums[i - 1]
            if (curr > 0 and last <= 0) or (curr < 0 and last >= 0):
                last = curr
                res += 1
        return res
