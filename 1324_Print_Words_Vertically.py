class Solution:
    def printVertically(self, s: str) -> List[str]:
        return [''.join(row).rstrip() for row in itertools.zip_longest(*s.split(), fillvalue=' ')]


class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(' ')
        n = max(len(word) for word in words)
        res = [''] * n
        for i in range(n):
            for j in range(len(words)):
                if i < len(words[j]):
                    res[i] += words[j][i]
                else:
                    res[i] += ' '
        for i in range(len(res)):
            t = len(res[i])
            for tw in res[i][::-1]:
                if tw == ' ':
                    t -= 1
                else:
                    break
            res[i] = res[i][:t]
        return res
