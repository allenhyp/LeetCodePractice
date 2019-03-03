class Solution:
    def isValid(self, S: str) -> bool:
        dp = {'a': 0, 'b': 0}
        for c in S:
            if c == 'a':
                dp['a'] += 1
            elif c == 'b' and dp['a'] > 0:
                dp['a'] -= 1
                dp['b'] += 1
            elif c == 'c' and dp['b'] > 0:
                dp['b'] -= 1
            else:
                return False
        if dp['a'] == 0 and dp['b'] == 0:
            return True
        return False
