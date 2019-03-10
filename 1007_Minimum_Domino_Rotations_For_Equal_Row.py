class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        d, target, real_target, a, b = {}, [], 0, 0, 0
        if len(A) < 2:
            return 0
        for i in range(2):
            d[A[0]] = d.get(A[0], 0) + 1
            d[B[0]] = d.get(B[0], 0) + 1
        for key, val in d.items():
            if val >= 2:
                target.append(key)
        if len(target) == 0:
            return -1
        elif len(target) == 2:
            for i in range(len(A)):
                if A[i] != target[0] and B[i] != target[0]:
                    real_target = target[1]
                    break
                elif A[i] != target[1] and B[i] != target[1]:
                    real_target = target[0]
        else:
            real_target = target[0]
        for i in range(len(A)):
            if A[i] != real_target and B[i] != real_target:
                return -1
            elif A[i] == B[i] == real_target:
                continue
            elif A[i] == real_target:
                a += 1
            else:
                b += 1
        return min(a, b)
