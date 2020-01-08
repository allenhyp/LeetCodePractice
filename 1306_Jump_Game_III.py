class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        def bfs(start):
            if start in visited:
                return False
            if arr[start] == 0:
                return True
            visited.add(start)
            res = False
            if start - arr[start] >= 0:
                res |= bfs(start - arr[start])
            if start + arr[start] < len(arr):
                res |= bfs(start + arr[start])
            return res
        return bfs(start)
