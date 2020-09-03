class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0: return False
        d = {}
        w = t + 1
        for i, v in enumerate(nums):
            m = v // w
            if ((m in d) or
                (m - 1 in d and abs(v - d[m - 1]) < w) or
                (m + 1 in d and abs(v - d[m + 1]) < w)):
                return True
            d[m] = v
            if i >= k: del d[nums[i - k] // w]
        return False
