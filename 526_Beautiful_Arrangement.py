class Solution:
    def countArrangement(self, N: int) -> int:
        def helper(nums, start):
            if start == 0:
                return 1
            count = 0
            for i in range(start, 0, -1):
                nums[start], nums[i] = nums[i], nums[start]
                if nums[start] % start == 0 or start % nums[start] == 0:
                    count += helper(nums, start - 1)
                nums[start], nums[i] = nums[i], nums[start]
            return count
        return helper([n for n in range(N + 1)], N)
