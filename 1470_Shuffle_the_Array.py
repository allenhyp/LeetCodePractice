class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ret = []
        for i in range(n):
            ret.extend([nums[i], nums[n + i]])
        return ret
