class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        n = len(A)
        left, right, s = [-1] * n, [n] * n, []
        for i in range(n):
            while len(s) and A[s[-1]] >= A[i]:
                tmp = s.pop()
                right[tmp] = i
            left[i] = s[-1] if len(s) else -1
            s.append(i)
            
        return sum(A[i] * (i - l) * (r - i) 
                   for i, (l, r) in enumerate(zip(left, right))) % (10 ** 9 + 7)
