# Binary search (O(mlogn))
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def bin_search(row):
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if row[mid] < 0:
                    right = mid
                else:
                    left = mid + 1
            return left
        res = 0
        for row in grid:
            res += n - bin_search(row)
        return res


# O(m + n)
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int: 
        m, n = len(grid), len(grid[0])
        res, r, c = 0, 0, n - 1
        while r < m and c >= 0:
            if grid[r][c] < 0:
                res += m - r
                c -= 1
            else:
                r += 1
        return res
