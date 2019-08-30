class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        dp = [T + 1] * (T + 1)
        dp[0] = 0
        for i in range(T + 1):
            for c in clips:
                if c[0] <= i <= c[1]:
                    dp[i] = min(dp[i], dp[c[0]] + 1)
        return -1 if dp[T] == T + 1 else dp[T]

class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        start, end, res = -1, 0, 0
        for s, e in sorted(clips):
            if end >= T or s > end:
                break
            elif start < s <= end:
                res, start = res + 1, end
            end = max(end, e)
        return res if end >= T else -1
