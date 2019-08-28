class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lon, cnt = [0] * n, [0] * n
        max_len = res = 0
        for i in range(n):
            lon[i] = cnt[i] = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    if lon[i] == lon[j] + 1:
                        cnt[i] += cnt[j]
                    if lon[i] < lon[j] + 1:
                        lon[i] = lon[j] + 1
                        cnt[i] = cnt[j]
            if max_len == lon[i]:
                res += cnt[i]
            if max_len < lon[i]:
                res = cnt[i]
                max_len = lon[i]
        return res
