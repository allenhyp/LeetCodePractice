class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return sorted([i for i in range(len(mat))], key=lambda x: (sum(mat[x]), x))[:k]
