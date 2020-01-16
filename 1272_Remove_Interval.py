class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        rl, rr = toBeRemoved
        for il, ir in intervals:
            if ir <= rl or il >= rr:
                res.append([il, ir])
            else:
                if il < rl:
                    res.append([il, rl])
                if rr < ir:
                    res.append([rr, ir])
        return res


class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        rl, rr = toBeRemoved
        for il, ir in intervals:
            if il < rl:
                res.append([il, min(ir, rl)])
            if rr < ir:
                res.append([max(il, rr), ir])
        return res
