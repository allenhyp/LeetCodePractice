class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        dic, res = {}, 0
        mod = 1000000007
        for i in range(len(arr)):
            res = (res + dic.get(target - arr[i], 0)) % mod
            for j in range(i):
                temp = arr[j] + arr[i]
                dic[temp] = dic.get(temp, 0) + 1
        return res
