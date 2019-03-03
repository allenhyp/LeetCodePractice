class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        start, res = 0, 0
        for i in range(len(A)):
            if A[i] == 0 and K:
                K -= 1
            elif A[i] == 0:
                while A[start] != 0:
                    start += 1
                start += 1              
            res = max(res, i - start + 1)
        return res
