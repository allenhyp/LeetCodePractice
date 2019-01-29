class Solution:
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if n == 0:
            return 0
        k = len(costs[0])
        if k == 0:
            return -1
        elif n == 1:
            return min(costs[0])
        prev_min, prev_min_idx, prev_sec_min = 0, -1, -1
        for i in range(n):
            cur_min, cur_min_idx, cur_sec_min = float('inf'), 0, float('inf')
            for j in range(k):
                val = costs[i][j] + (prev_sec_min if j == prev_min_idx else prev_min)
                if val < cur_min:
                    cur_sec_min = cur_min
                    cur_min = val
                    cur_min_idx = j
                elif val < cur_sec_min:
                    cur_sec_min = val
            prev_min, prev_min_idx, prev_sec_min = cur_min, cur_min_idx, cur_sec_min
        return prev_min
