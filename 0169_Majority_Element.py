class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major, cnt = nums[0], 1
        for i in range(1, len(nums)):
            if cnt == 0:
                major, cnt = nums[i], 1
            elif major == nums[i]:
                cnt += 1
            else:
                cnt -= 1
        return major
