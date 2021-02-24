class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        def searchRec(top, bottom, left, right):
            if top > bottom or left > right:
                return False
            elif target < matrix[top][left] or target > matrix[bottom][right]:
                return False
            mid = (left + right) // 2
            row = top
            while row <= bottom and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            return searchRec(row, bottom, left, mid - 1) or searchRec(top, row - 1, mid + 1, right)
        return searchRec(0, len(matrix) - 1, 0, len(matrix[0]) - 1)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        j = -1
        for row in matrix:
            while j + len(row) and row[j] > target:
                j -= 1
            if row[j] == target:
                return True
        return False
