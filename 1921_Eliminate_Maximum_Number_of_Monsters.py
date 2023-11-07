class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrivals = sorted([dist[i]/speed[i] for i in range(len(dist))])
        for i, arrival in enumerate(arrivals):
            if arrival <= i:
                return i
        return len(arrivals)
