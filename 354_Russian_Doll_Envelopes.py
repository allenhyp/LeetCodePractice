class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        widths, lis = [w for h, w in envelopes], []
        # longest increasing subsequence
        for width in widths:
            idx = bisect.bisect_left(lis, width)
            lis[idx:idx + 1] = [width]
        return len(lis)
