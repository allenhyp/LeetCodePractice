class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        lookup = {-1: set()}
        for num in sorted(nums):
            lookup[num] = max((lookup[d] for d in lookup if num % d == 0), key=len) | {num}
        return list(max(lookup.values(), key=len))
