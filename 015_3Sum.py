class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums, res = sorted(nums), set()
        for idx, val in enumerate(nums[:-2]):
            if idx > 0 and val == nums[idx - 1]:
                continue
            d = {}
            for x in nums[idx + 1:]:
                if x not in d:
                    d[-val - x] = 1
                else:
                    res.add((val, -val - x, x))
        return list(map(list, res))
