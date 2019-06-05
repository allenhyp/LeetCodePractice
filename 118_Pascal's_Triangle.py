class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows):
            res.append(list(map(lambda x, y: x+y, [0] + res[-1], res[-1] + [0])))
        return res[:numRows]
