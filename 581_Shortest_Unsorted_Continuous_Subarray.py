class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left, right = len(nums), 0
        for i, v in enumerate(sorted(nums)):
            if nums[i] != v:
                left = min(left, i)
                right = max(right, i)
        return (right - left + 1) if right - left >= 0 else 0


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left, right = len(nums), 0
        stack = []
        for i, v in enumerate(nums):
            while stack and nums[stack[-1]] > v:
                left = min(left, stack.pop())
            stack.append(i)
        stack = []
        for i, v in reversed(list(enumerate(nums))):
            while stack and nums[stack[-1]] < v:
                right = max(right, stack.pop())
            stack.append(i)
        return right - left + 1 if right - left > 0 else 0
