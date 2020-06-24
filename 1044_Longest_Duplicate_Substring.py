class Solution:
    def search(self, L, base, n, mod, nums):
        h = 0
        for a in nums[:L]:
            h = (h * base + a) % mod
        seen = {h}
        baseL = (base ** (L - 1)) % mod
        for start in range(1, n - L + 1):
            h = ((h - nums[start - 1] * baseL) * base + nums[start + L - 1]) % mod
            if h in seen:
                return start
            seen.add(h)
        return -1
    
    def longestDupSubstring(self, S: str) -> str:
        nums = [ord(s) - ord('a') for s in S]
        base = 26
        n = len(S)
        mod = 2 ** 32
        left, right = 1, n
        while left <= right:
            L = (left + right) // 2
            if self.search(L, base, n, mod, nums) != -1:
                left = L + 1
            else:
                right = L - 1
        start = self.search(left - 1, base, n, mod, nums)
        return S[start:start + left - 1]
