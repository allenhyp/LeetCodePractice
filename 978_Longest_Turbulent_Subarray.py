class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        c = []
        n = len(A)
        for i in range(n - 1):
            if A[i] < A[i + 1]:
                c.append(1)
            elif A[i] == A[i + 1]:
                c.append(0)
            else:
                c.append(-1)
        i, j, longest= -1, 0 , 1
        while j < n - 2:
            while c[j] == 0:
                j += 1
                if j >= n - 2:
                    return longest
            i = j + 1
            cur = c[j]
            while i < n - 1 and c[i] != cur and c[i] != 0:
                cur = c[i]
                i += 1
            longest = max(longest, i - j + 1)
            j = i
        return longest
