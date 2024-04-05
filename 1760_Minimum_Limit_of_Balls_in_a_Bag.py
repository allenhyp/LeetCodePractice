class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def isPossible(nums, maxOperations, penalty):
            reqOps = 0
            for num in nums:
                op = num // penalty - (1 if num%penalty==0 else 0)
                reqOps += op
            return reqOps <= maxOperations
        
        start, end = 1, max(nums)
        while start < end:
            penalty = (start + end) // 2
            if isPossible(nums, maxOperations, penalty):
                end = penalty
            else:
                start = penalty + 1
        return start
