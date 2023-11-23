class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n, m = len(nums), len(l)
        ret = []
        for i in range(m):
            arr = sorted(nums[l[i]:r[i]+1])
            for j in range(2, len(arr)):
                if arr[j] - arr[j-1] != arr[j-1] - arr[j-2]:
                    ret.append(False)
                    break
            else:
                ret.append(True)
        return ret
