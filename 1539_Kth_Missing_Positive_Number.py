class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        last = 0
        for num in arr:
            if k > num - last - 1:
                k -= num - last - 1
            else:
                return last + k
            last = num
        return last + k
