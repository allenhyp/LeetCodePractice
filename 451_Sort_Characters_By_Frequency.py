class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        bucket = [[] for _ in range(len(s) + 1)]
        res = ''

        for c in s:
            dic[c] = dic.get(c, 0) + 1
        for key, feq in dic.items():
            bucket[feq].append(key)
        for feq, chars in enumerate(bucket[::-1]):
            for c in chars:
                for _ in range(len(s) - feq):
                    res += c
        return res


class Solution:
    def frequencySort(self, s: str) -> str:
        res = ""
        for key, val in sorted(collections.Counter(s).items(), key=lambda x: -x[1]):
            res += key * val
        return res
        