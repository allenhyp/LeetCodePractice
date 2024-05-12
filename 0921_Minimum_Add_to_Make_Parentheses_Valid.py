class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opens = closes = 0
        for p in s:
            if p == '(':
                opens += 1
            elif p == ')':
                if opens > 0:
                    opens -= 1
                else:
                    closes += 1
        return opens + closes
