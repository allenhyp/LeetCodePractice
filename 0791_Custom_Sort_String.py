class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = collections.Counter(s)
        res = []
        for k in order:
            if counter[k] > 0:
                res.extend([k] * counter[k])
                del counter[k]
        for k, v in counter.items():
            res.extend([k] * v)
        return ''.join(res)
