class Solution:
    def maxArea(self, h: int, w: int, H: List[int], V: List[int]) -> int:
        mh, mv = 0, 0
        H = [0] + sorted(H) + [h]
        V = [0] + sorted(V) + [w]
        for i in range(1, len(H)):
            mh = max(mh, H[i] - H[i - 1])
        for j in range(1, len(V)):
            mv = max(mv, V[j] - V[j - 1])
        return (mh * mv) % (10 ** 9 + 7)
