class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ns, np = len(s), len(p)
        match = [[False] * (np + 1) for _ in range(ns + 1)]
        match[ns][np] = True
        for i in range(np - 1, -1, -1):
            if p[i] != '*':
                break
            else:
                match[ns][i] = True
        for i in range(ns - 1, -1, -1):
            for j in range(np - 1, -1, -1):
                if s[i] == p[j] or p[j] == '?':
                    match[i][j] = match[i + 1][j + 1]
                elif p[j] == '*':
                    match[i][j] = match[i + 1][j] | match[i][j + 1]
                else:
                    match[i][j] = False
        return match[0][0]
