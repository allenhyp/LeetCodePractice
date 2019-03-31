class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        num = 0
        for a in A:
            num = (num << 1) + a
            res.append(True if num % 5 == 0 else False)
        return res
