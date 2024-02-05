class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for (int i = 0; i < 9; i++) {
            set<char> lookup({'1', '2', '3', '4', '5', '6', '7', '8', '9'});
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') continue;
                if (lookup.find(board[i][j]) == lookup.end()) return false;
                else lookup.erase(board[i][j]);
            }
        }
        for (int i = 0; i < 9; i++) {
            set<char> lookup({'1', '2', '3', '4', '5', '6', '7', '8', '9'});
            for (int j = 0; j < 9; j++) {
                if (board[j][i] == '.') continue;
                if (lookup.find(board[j][i]) == lookup.end()) return false;
                else lookup.erase(board[j][i]);
            }
        }
        for (int i = 0; i < 9; i += 3) {
            for (int j = 0; j < 9; j += 3) {
                set<char> lookup({'1', '2', '3', '4', '5', '6', '7', '8', '9'});
                for (int di = 0; di < 3; di++) {
                    for (int dj = 0; dj < 3; dj++) {
                        if (board[i+di][j+dj] == '.') continue;
                        if (lookup.find(board[i+di][j+dj]) == lookup.end()) return false;
                        else lookup.erase(board[i+di][j+dj]);
                    }
                }
            }
        }
        return true;
    }
};
