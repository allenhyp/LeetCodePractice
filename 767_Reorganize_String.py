class Solution:
    def reorganizeString(self, S: str) -> str:
        most = collections.Counter(S).most_common()
        res = [most[0][0]] * most[0][1]
        idx = 0
        for ch, count in most[1:]:
            for _ in range(count):
                res[idx % most[0][1]] += ch
                idx += 1
        return "".join(res) if idx >= most[0][1] - 1 else ""
