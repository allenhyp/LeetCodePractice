class Solution:
    def numberOfArithmeticSlices(self, A: 'List[int]') -> 'int':
        dp = res = 0
        for i in range(len(A) - 2):
            if A[i + 1] - A[i] == A[i + 2] - A[i + 1]:
                dp += 1
                res += dp
            else:
                dp = 0
        return res
