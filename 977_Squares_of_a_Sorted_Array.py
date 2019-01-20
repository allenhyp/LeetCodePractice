class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        pos = 0
        n = len(A)
        res = []
        for i in range(n):
            pos = i
            if A[i] >= 0:
                break
        i, j = pos, pos - 1
        while i < n and j >= 0:
            ps = A[i] ** 2
            ns = A[j] ** 2
            if ps < ns:
                res.append(ps)
                i += 1
            else:
                res.append(ns)
                j -= 1
        while i < n:
            res.append(A[i] ** 2)
            i += 1
        while j >= 0:
            res.append(A[j] ** 2)
            j -= 1
        return res    
