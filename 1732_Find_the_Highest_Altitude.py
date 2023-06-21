class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur = alt = 0
        for g in gain:
            cur += g
            if cur > alt:
                alt = cur
        return alt
