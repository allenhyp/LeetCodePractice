class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        acc, cur, div, size = [0], 0, 2*k+1, len(nums)
        ret = [-1] * size
        for n in nums:
            cur += n
            acc.append(cur)
        
        for i in range(k, size-k):
                ret[i] = (acc[i+k+1] - acc[i-k]) // div
        
        return ret
