class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] = arr[i - 1] ^ arr[i]
        res = []
        for query in queries:
            res.append(arr[query[1]] if query[0] == 0 else arr[query[1]] ^ arr[query[0] - 1])
        return res
