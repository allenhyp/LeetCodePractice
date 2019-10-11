class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        dic = {}
        count = 0
        for a in A:
            for b in B:
                s = a + b
                dic[s] = dic.get(s, 0) + 1     
        for c in C:
            for d in D:
                s = c + d
                count += dic.get(-s, 0)
        return count
