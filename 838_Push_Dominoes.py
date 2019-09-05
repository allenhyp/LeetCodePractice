class Solution:
    def pushDominoes(self, d: str) -> str:
        d = 'L' + d + 'R'
        res, i = [], 0
        for j in range(1, len(d)):
            if d[j] == '.':
                continue
            n = j - i - 1
            if i:
                res.append(d[i])
            if d[i] == d[j]:
                res.append(n * d[j])
            elif d[i] == 'L' and d[j] == 'R':
                res.append(n * '.')
            else:
                res.append((n // 2) * 'R' + (n % 2) * '.' + (n // 2) * 'L')
            i = j
        return ''.join(res)
