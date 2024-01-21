# Monotonic Stack
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        stack = []
        left = [-1] * n
        for i in range(n - 1, -1, -1):
            while stack and arr[i] < arr[stack[-1]]:
                left[stack.pop()] = i
            stack.append(i)

        stack = []
        right = [n] * n
        for i in range(n):
            while stack and arr[i] <= arr[stack[-1]]:
                right[stack.pop()] = i
            stack.append(i)

        ret = 0
        for i in range(n):
            ret += arr[i] * (i - left[i]) * (right[i] - i)
        return ret % (10**9+7)


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
