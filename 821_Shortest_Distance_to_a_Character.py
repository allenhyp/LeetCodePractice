class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        dis, n = inf, len(s)
        res = [inf] * n
        for i in range(n):
            if s[i] == c:
                bdis = 0
                for j in range(i, -1, -1):
                    if bdis >= res[j]: break
                    res[j], bdis = bdis, bdis + 1
                dis = 1
            else:
                res[i], dis = dis, dis + 1
        return res
