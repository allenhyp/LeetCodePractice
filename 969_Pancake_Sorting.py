class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        # Find the maximum number then flip twice to put it to tail
        res = []
        for m in range(len(A), 1, -1):
            idx = A.index(max(A[:m]))
            if idx + 1 == m:
                continue
            elif idx == 0:
                res.append(m)
                A = A[m - 1::-1] + A[m:]
            else:
                res.extend([idx + 1, m])
                A = A[m - 1:idx:-1] + A[:idx + 1] + A[m:]
        return res
