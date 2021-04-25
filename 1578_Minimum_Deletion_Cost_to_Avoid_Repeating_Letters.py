class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        pre = res = 0
        for cur in range(1, len(s)):
            if s[pre] == s[cur]:
                if cost[pre] < cost[cur]:
                    res += cost[pre]
                    pre = cur
                else:
                    res += cost[cur]
            else:
                pre = cur
        return res
