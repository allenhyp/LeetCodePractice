class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        c = collections.Counter()
        res = 0
        for t in time:
            res += c[-t % 60]
            c[t % 60] += 1
        return res

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res, d = 0, {}
        for song in time:
            for target in range(60, 961, 60):
                if (target - song) in d:
                    res += d[target - song]
            d[song] = d.get(song, 0) + 1
        return res
