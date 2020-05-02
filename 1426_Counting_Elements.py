class Solution:
    def countElements(self, arr: List[int]) -> int:
        visited = set(arr)
        res = 0
        for a in arr:
            if a + 1 in visited:
                res += 1
        return res
