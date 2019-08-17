# Dynamic Programming
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        memo = {}
        def dp(i, j):
            if j <= i:
                return 0
            if (i, j) not in memo.keys():
                res = float('inf')
                for k in range(i + 1, j + 1):
                    res = min(res, dp(i, k - 1) + dp(k, j) + max(arr[i : k]) * max(arr[k : j + 1]))
                memo[(i, j)] = res
            return memo[(i, j)]
        return dp(0, len(arr) - 1)

# Greedy
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack, n, res = [float('inf')], len(arr), 0
        for a in arr:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res
