class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dic = {}
        res = 0
        for num in nums:
            if dic.get(k - num, 0) > 0:
                dic[k - num] -= 1
                res += 1
            else:
                dic[num] = dic.get(num, 0) + 1
        return res
