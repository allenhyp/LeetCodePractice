class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ret = []
        def backtracking(current, index):
            if index == len(nums):
                self.ret.append(current)
                return
            backtracking(current, index + 1)
            backtracking(current + [nums[index]], index + 1)
        backtracking([], 0)
        return self.ret
