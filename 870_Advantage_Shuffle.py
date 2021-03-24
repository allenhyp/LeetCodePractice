class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A = sorted(A)
        take = collections.defaultdict(list)
        for b in sorted(B)[::-1]:
            if A[-1] > b:
                take[b].append(A.pop())
        return [(take[b] or A).pop() for b in B]
