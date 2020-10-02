class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        cur_min, cur_max, res = arrays[0][0], arrays[0][-1], 0
        for arr in arrays[1:]:
            res = max(res, abs(cur_min - arr[-1]), abs(cur_max - arr[0]))
            cur_min, cur_max = min(cur_min, arr[0]), max(cur_max, arr[-1])
        return res
