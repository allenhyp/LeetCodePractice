from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = defaultdict(list)
        for i in range(len(groupSizes)):
            dic[groupSizes[i]].append(i)
        res = []
        for key, val in dic.items():
            for i in range(0, len(val), key):
                res.append(val[i:i + key])
        return res
