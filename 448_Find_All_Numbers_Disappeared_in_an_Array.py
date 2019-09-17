class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums) + 1)) - set(nums))

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            tmp = abs(nums[i]) - 1
            nums[tmp] = -nums[tmp] if nums[tmp] > 0 else nums[tmp]
        res = []
        for i in range(n):
            if nums[i] > 0:
                res.append(i + 1)
        return res
