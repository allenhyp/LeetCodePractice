from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        diff = defaultdict(int)
        ret = []
        for c in p:
            diff[c] -= 1
        
        for c in s[:n]:
            diff[c] += 1
        
        def checkMatch(diff):
            for v in diff.values():
                if v != 0:
                    return False
            return True
        
        if checkMatch(diff):
            ret.append(0)

        for i in range(n, len(s)):
            diff[s[i - n]] -= 1
            diff[s[i]] += 1
            if checkMatch(diff):
                ret.append(i - n + 1)

        return ret
