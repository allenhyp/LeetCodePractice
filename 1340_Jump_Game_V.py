# Top-down with memo (O(nd))
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [0] * n
        def dfs(i):
            if dp[i] > 0: return dp[i]
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dfs(j) + 1)
                else: break
            for j in range(i - 1, max(i - d - 1, -1), -1):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dfs(j) + 1)
                else: break
            return dp[i] if dp[i] > 0 else 1
        for i in range(n):
            dp[i] = dfs(i)
        return max(dp)


# Speed up with stack and dic
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        graph = collections.defaultdict(set)
        def search(iterator):
            stack = []
            for i in iterator:
                while stack and abs(i - stack[-1]) <= d and arr[stack[-1]] < arr[i]:
                    graph[stack.pop()].add(i)
                stack.append(i)
        search(range(n))
        search(range(n)[::-1])
        memo = {}
        def dfs(i):
            res = 0
            if i not in memo:
                for j in graph[i]:
                    res = max(res, 1 + dfs(j))
                memo[i] = res
            return memo[i]
        return 1 + max([dfs(i) for i in range(n)])
        