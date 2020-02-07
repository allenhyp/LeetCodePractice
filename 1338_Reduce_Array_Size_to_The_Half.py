class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = collections.Counter(arr)
        target, cur, res = len(arr) // 2, 0, 0
        for v in sorted(counter.values(), reverse=True):
            cur, res = cur + v, res + 1
            if  cur >= target:
                break
        return res
