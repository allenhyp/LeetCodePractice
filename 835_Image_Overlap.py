class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        la = [(i, j) for i in range(len(A)) for j in range(len(A[0])) if A[i][j] == 1]
        lb = [(i, j) for i in range(len(B)) for j in range(len(B[0])) if B[i][j] == 1]
        d = collections.defaultdict(int)
        maximum = 0
        for a in la:
            for b in lb:
                dist = (a[0] - b[0], a[1] - b[1])
                d[dist] += 1
                maximum = max(maximum, d[dist])
        return maximum
