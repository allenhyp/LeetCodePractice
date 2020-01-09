class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s) - 1
        res = []
        while i > -1:
            if s[i] == '#':
                res.append(chr(int(s[i - 2:i]) + 96))
                i -= 3
            else:
                res.append(chr(int(s[i]) + 96))
                i -= 1
        return "".join(res[::-1])
