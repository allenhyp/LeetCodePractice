class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        for r in s[::-1].split(' '):
            if r != '':
                res.append(r[::-1])
        return ' '.join(res)
