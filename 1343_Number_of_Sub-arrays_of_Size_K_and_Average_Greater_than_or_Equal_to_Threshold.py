class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left, window, res, target = -1, 0, 0, threshold * k
        for cur, v in enumerate(arr):
            window += v
            if cur - left == k:
                res += 1 if window >= target else 0
                left += 1
                window -= arr[left]
        return res
