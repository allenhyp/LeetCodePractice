class Solution:
    @cache
    def kInversePairs(self, n: int, k: int) -> int:
        if k == 0:
            return 1
        if n == 0:
            return 0
        # f(n, k) = f(n-1, k) + f(n-1, k) - max(0, f(n-1, k-n))1000000007
        return (self.kInversePairs(n, k-1) + self.kInversePairs(n-1, k) 
                - (0 if k - n < 0 else self.kInversePairs(n-1, k-n))) % 1000000007
