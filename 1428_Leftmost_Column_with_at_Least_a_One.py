# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()
        def find(row):
            start, end, pos = 0, m - 1, n
            while start <= end:
                mid = (start + end) // 2
                if binaryMatrix.get(row, mid) == 0:
                    start = mid + 1
                else:
                    pos, end = mid, mid - 1
            return pos
        
        res = n
        for i in range(n):
            res = min(res, find(i))
        return res if res < n else -1


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        r, c = 0, cols - 1
        while r < rows and c >= 0:
            if binaryMatrix.get(r, c) == 0:
                r += 1
            else:
                c -= 1
        return c + 1 if c != cols - 1 else -1
