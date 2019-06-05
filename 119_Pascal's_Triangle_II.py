class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(rowIndex):
            res = list(map(lambda x, y: x+y, [0] + res, res + [0]))
        return res
