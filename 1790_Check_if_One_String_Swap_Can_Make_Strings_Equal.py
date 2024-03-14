from collections import Counter
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        cnt1, cnt2 = Counter(s1), Counter(s2)
        if cnt1 != cnt2: return False
        dis = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                dis += 1
        if dis == 0 or dis == 2:
            return True
        return False
