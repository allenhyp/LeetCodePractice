from collections import Counter
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        ret = 0
        for _, v in counter.items():
            if v == 1:
                return -1
            ret += ceil(v / 3)
        return ret
