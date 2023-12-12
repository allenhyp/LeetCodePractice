class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def helper(matrix, t, b, l, r):
            if t > b or l > r:
                return []
            if t == b and l == r:
                return [matrix[t][l]]
            if t == b:
                return matrix[t][l:r + 1]
            if l == r:
                return [matrix[i][l] for i in range(t, b + 1)]
            
            ret = []
            for w in range(l, r):
                ret.append(matrix[t][w])
            for x in range(t, b):
                ret.append(matrix[x][r])
            for y in range(r, l, -1):
                ret.append(matrix[b][y])
            for z in range(b, t, -1):
                ret.append(matrix[z][l])
            return ret + helper(matrix, t + 1, b - 1, l + 1, r - 1)
        t, b, l, r = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        return helper(matrix, t, b, l, r)
