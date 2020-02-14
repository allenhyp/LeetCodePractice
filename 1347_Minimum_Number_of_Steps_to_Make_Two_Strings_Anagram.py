class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_cnt = collections.Counter(s)
        t_cnt = collections.Counter(t)
        res = 0
        for c in s_cnt.keys():
            if c in t_cnt:
                if s_cnt[c] - t_cnt[c] > 0:
                    res += s_cnt[c] - t_cnt[c]
            else:
                res += s_cnt[c]
        return res
