class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def enough(x):
            return sum(min(x // i, n) for i in range(1, m + 1)) >= k
        
        low, high = 1, m * n
        while (low < high):
            mid = (low + high) // 2
            if enough(mid):
                high = mid
            else:
                low = mid + 1
        return high
