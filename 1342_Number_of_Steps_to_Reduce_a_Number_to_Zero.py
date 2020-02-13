class Solution:
    def numberOfSteps (self, num: int) -> int:
        res = 0
        while num > 0:
            res += 2 if num & 1 else 1
            num >>= 1
        return res - 1
