class Solution:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.isWord = False
            
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = self.TrieNode()
        for word in words:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = self.TrieNode()
                cur = cur.children[c]
            cur.isWord = True
        
        m, n = len(board), len(board[0])
        self.res = []
        self.dir = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        def dfs(i, j, node, path):                
            if 0 <= i < m and 0 <= j < n:
                if board[i][j] in node.children:
                    nxt = node.children[board[i][j]]
                    path += board[i][j]
                    temp, board[i][j] = board[i][j], '*'
                    if nxt.isWord:
                        self.res.append(path)
                        nxt.isWord = False
                    for di, dj in self.dir:
                        dfs(i + di, j + dj, nxt, path)
                    board[i][j] = temp
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, root, '')
        
        return self.res
