class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = 0
        for n in nums:
            diff ^= n
        # ~(diff - 1) = -(diff - 1) = -diff
        diff &= -diff
        res = [0, 0]
        for n in nums:
            res[0 if n & diff == 0 else 1] ^= n
        return res
