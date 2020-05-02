class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        direction = amount = 0
        for d, a in shift:
            if d == direction:
                amount += a
            else:
                if amount >= a:
                    amount -= a
                else:
                    direction, amount = d, a - amount
        amount %= len(s)
        if direction:
            return s[-amount:] + s[:-amount]
        else:
            return s[amount:] + s[:amount]
