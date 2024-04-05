class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        postMax = 0
        res = []
        for i in range(len(heights)-1, -1, -1):
            height = heights[i]
            if height > postMax:
                res.append(i)
            postMax = max(postMax, height)
        return res[::-1]
