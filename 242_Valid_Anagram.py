from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = defaultdict(int)
        for c in s:
            map[c] += 1
        for c in t:
            if c in map and map[c] > 0:
                map[c] -= 1
            else:
                return False
        for _, v in map.items():
            if v != 0:
                return False
        return True
