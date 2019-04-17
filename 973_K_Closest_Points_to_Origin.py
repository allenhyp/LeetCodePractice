class Solution:
    def quickSelect(self, k, start, end):
        if start >= end:
            return
        l, r, pivot = start, end, (start + end) // 2
        dist = self.points[pivot][0] ** 2 + self.points[pivot][1] ** 2
        while l <= r:
            distL = self.points[l][0] ** 2 + self.points[l][1] ** 2
            distR = self.points[r][0] ** 2 + self.points[r][1] ** 2
            while l <= r and distL < dist:
                l += 1
                distL = self.points[l][0] ** 2 + self.points[l][1] ** 2
            while l <= r and distR > dist:
                r -= 1
                distR = self.points[r][0] ** 2 + self.points[r][1] ** 2
            if l <= r:
                self.points[l], self.points[r] = self.points[r], self.points[l]
                l, r = l + 1, r - 1
        if k - 1 <= r:
            self.quickSelect(k, start, r)
        if k - 1 >= l:
            self.quickSelect(k, l, end)   
        
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        self.points = points
        self.quickSelect(K, 0, len(points) - 1)
        return self.points[:K]
