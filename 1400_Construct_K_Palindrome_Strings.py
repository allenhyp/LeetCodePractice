class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k: return False
        cnt = collections.Counter(s)
        odds = 0
        for c, v in cnt.items():
            if v % 2 == 1:
                odds += 1
        return odds <= k
