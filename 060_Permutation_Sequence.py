from math import factorial
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n + 1)]
        k -= 1
        res = ''
        for i in range(n - 1, -1, -1):
            index, k = divmod(k, factorial(i))
            res += str(nums[index])
            nums.remove(nums[index])
        return res
