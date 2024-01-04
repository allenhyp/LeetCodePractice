class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs(r, c, index, visited):
            if not (0 <= r < m and 0 <= c < n):
                return False
            if (r, c) in visited:
                return False
            if board[r][c] == word[index]:
                if index == len(word) - 1:
                    return True
                
                visited.add((r, c))
                ret = False
                for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    ret |= dfs(r + dr, c + dc, index + 1, visited)
                visited.remove((r,c))
                return ret

            return False

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0, set()):
                    return True
        return False
