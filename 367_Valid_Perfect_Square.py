class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start, end = 0, num
        while start <= end:
            mid = (start + end) // 2
            mid2 = mid * mid
            if mid2 == num:
                return True
            elif mid2 > num:
                end = mid - 1
            else:
                start = mid + 1
        return False
