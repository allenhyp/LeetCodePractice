class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs(i, j, k):
            if 0 <= i < m and 0 <= j < n:
                if board[i][j] == word[k]:
                    if k == len(word) - 1:
                        return True
                    result = False
                    temp = board[i][j]
                    board[i][j] = '*'
                    for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                        result |= dfs(i + di, j + dj, k + 1)
                    board[i][j] = temp
                    return result
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
