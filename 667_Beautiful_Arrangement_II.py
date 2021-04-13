class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = [i for i in range(1, n + 1)]
        for i in range(1, k):
            res = res[:i] + res[-1:i - 1:-1]
        return res
