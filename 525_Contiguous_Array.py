class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {0: 0}
        maximum = count = 0
        for i, num in enumerate(nums, 1):
            count += 1 if num == 1 else -1
            if count in dic:
                maximum = max(maximum, i - dic[count])
            else:
                dic[count] = i
        return maximum
