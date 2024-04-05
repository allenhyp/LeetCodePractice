class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        f = s = 0
        res = []
        while f < len(firstList) and s < len(secondList):
            if firstList[f][0] > secondList[s][1]:
                s += 1
            elif firstList[f][1] < secondList[s][0]:
                f += 1
            else:
                res.append([max(firstList[f][0], secondList[s][0]), min(firstList[f][1], secondList[s][1])])
                f, s = f+(1 if firstList[f][1] <= secondList[s][1] else 0), s+(1 if secondList[s][1] <= firstList[f][1] else 0)
        return res
