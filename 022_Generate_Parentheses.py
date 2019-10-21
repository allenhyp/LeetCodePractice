class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtracking(_str, _open, _close):
            if (len(_str) == 2 * n):
                res.append(_str)
                return
            if (_open < n):
                backtracking(_str + '(', _open + 1, _close)
            if (_close < _open):
                backtracking(_str + ')', _open, _close + 1)
        backtracking("", 0, 0)
        return res
