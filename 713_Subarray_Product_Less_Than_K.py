class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        cur, i, j, res = 1, 0, 0, 0
        for j in range(len(nums)):
            cur *= nums[j]
            while i <= j and cur >= k:
                cur /= nums[i]
                i += 1
            res += j - i + 1
        return res
