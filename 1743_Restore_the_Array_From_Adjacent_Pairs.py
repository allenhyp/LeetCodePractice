class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        dic, n, res = collections.defaultdict(list), len(adjacentPairs) + 1, []
        for pair in adjacentPairs:
            dic[pair[0]].append(pair[1])
            dic[pair[1]].append(pair[0])
        for k, v in dic.items():
            if len(v) == 1:
                cur = k
                break
        pre = cur
        res.append(cur)
        while len(res) < n:
            for num in dic[cur]:
                if num != pre:
                    res.append(num)
                    pre = cur
                    cur = num
                    break
        return res
