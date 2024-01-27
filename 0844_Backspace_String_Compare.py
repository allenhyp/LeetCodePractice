class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(s):
            _s = []
            for c in s:
                if c != '#':
                    _s.append(c)
                elif _s:
                    _s.pop()
            return _s

        return process(s) == process(t)
