class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res, md = -1, float('inf')
        for i, p in enumerate(points):
            if p[0] == x or p[1] == y:
                d = abs(p[0]-x) + abs(p[1]-y)
                if d < md:
                    md = d
                    res = i
        return res
