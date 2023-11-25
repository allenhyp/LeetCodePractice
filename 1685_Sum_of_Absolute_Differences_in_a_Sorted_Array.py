class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix, suffix, n = [nums[0]], [nums[-1]], len(nums)
        for i in range(1, n):
            prefix.append(nums[i] + prefix[i - 1])
            suffix.insert(0, nums[n - 1 - i] + suffix[0])
        
        return [nums[i] * (2*i-n+1) 
            - (prefix[i-1] if i > 0 else 0)
            + (suffix[i+1] if i < n-1 else 0)
            for i in range(n)]
