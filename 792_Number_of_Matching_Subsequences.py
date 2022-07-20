from collections import defaultdict
from bisect import bisect_right
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ret = 0
        lookup = defaultdict(list)
        for i, c in enumerate(s):
            lookup[c].append(i)
        for word in words:
            cur, found = -1, True
            for w in word:
                idx = bisect_right(lookup[w], cur)
                if idx >= len(lookup[w]):
                    found = False
                    break
                else:
                    cur = lookup[w][idx]
            if found:
                ret += 1
        return ret
