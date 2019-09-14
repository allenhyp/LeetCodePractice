class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        swap, not_swap, n = 1, 0, len(A)
        for i in range(1, n):
            st = nt = n
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                st, nt = swap + 1, not_swap
            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                st, nt = min(st, not_swap + 1), min(nt, swap)
            swap, not_swap = st, nt
        return min(swap, not_swap)
