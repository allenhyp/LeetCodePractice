class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        for a in sorted(arr):
            rank.setdefault(a, len(rank) + 1)
        return map(rank.get, arr)


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        return map({a: i + 1 for i, a in enumerate(sorted(set(arr)))}.get, arr)
