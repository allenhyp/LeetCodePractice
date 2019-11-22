class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s, res= [], [-1] * n
        for i in range(2 * n):
            cur = nums[i % n]
            while len(s) and nums[s[-1]] < cur:
                res[s.pop()] = cur
            s.append(i % n)
        return res
