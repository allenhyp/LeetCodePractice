class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        intersection = points[0]
        res = 0
        for point in points:
            if point[0] <= intersection[1]:
                intersection[0] = max(point[0], intersection[0])
                intersection[1] = min(point[1], intersection[1])
            else:
                res += 1
                intersection = point
        
        return res+1
