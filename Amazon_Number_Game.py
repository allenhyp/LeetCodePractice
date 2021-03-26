class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        
        @lru_cache(None)
        def dfs(i, mask):  # mask means if certain numbers are already used
            if i > n // 2:
                return 0
            res = 0
            for j in range(n):
                for k in range(j + 1, n):
                    new_mask = (1 << j) | (1 << k)
                    if (mask & new_mask) == 0: # check duplicate numbers
                        sum_ = i * gcd(nums[j], nums[k]) + dfs(i + 1, mask | new_mask)
                        res = max(res, sum_)
            return res
        
        return dfs(1, 0)

'''
Time: 
O((n^2) * (2^n)) because of two nested loops which causes n^2 time complexity.

O(n * n! / ∑ i! (n - i)!), where i in [2, 4, ... n - 2]. On each step, we can choose 2 options from the remaining ones. 
So, for the first step we can have C(14, 2) options, on the second - C(14, 4) options and so on. Here are the actual numbers 
for each step 1 to 7 (total 8191 operations):

Step 1: 1
Step 2: 91
Step 3: 1001
Step 4: 3003
Step 5: 3003
Step 6: 1001
Step 7: 91

Memory: O(n * 2 ^ n) for the memoisation since we use an array.
'''
