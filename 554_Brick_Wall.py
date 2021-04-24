class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall)
        edges = collections.defaultdict(int)
        minimum = n
        for bricks in wall:
            width = 0
            for brick in bricks[:-1]:
                width += brick
                edges[width] += 1
                minimum = min(minimum, n - edges[width])
        return minimum
