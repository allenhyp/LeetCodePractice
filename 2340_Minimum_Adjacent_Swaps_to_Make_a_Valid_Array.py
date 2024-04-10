class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        min_val = min(nums)
        min_index = nums.index(min_val)
        nums = [min_val] + nums[:min_index] + nums[min_index+1:]
        max_val = max(nums)
        max_reversed_index = nums[::-1].index(max_val)
        return min_index + max_reversed_index
