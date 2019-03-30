class Solution {
private:
    int m, n, w;
    vector<vector<int>> directions = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
    bool dfs(vector<vector<char>>& board, string word, int i, int j, int k) {
        if (i >= 0 && i < m && j >= 0 && j < n) {
            if (board[i][j] == word[k]) {
                if (++k == w) return true;
                char temp = board[i][j];
                board[i][j] = '*';
                for (auto dir : directions) {
                    if (dfs(board, word, i + dir[0], j + dir[1], k))
                        return true;
                }
                board[i][j] = temp;
            }
        }
        return false;
    }
public:
    bool exist(vector<vector<char>>& board, string word) {
        m = board.size();
        n = board[0].size();
        w = word.size();
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (dfs(board, word, i, j, 0))
                    return true;
            }
        }
        return false;
    }
};
