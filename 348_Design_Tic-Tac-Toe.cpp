class TicTacToe {
private:
    vector<int> row, col;
    int diag, anti, width;
public:
    /** Initialize your data structure here. */
    TicTacToe(int n) {
        width = n;
        row = vector<int>(n, 0);
        col = vector<int>(n, 0);
        diag = 0, anti = 0;
    }
    
    /** Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins. */
    int move(int r, int c, int player) {
        int flag = player == 1 ? 1 : -1;
        row[r] += flag;
        col[c] += flag;
        if (r == c) diag += flag;
        if (r + c == width - 1) anti += flag;
        if (row[r] == width || col[c] == width || diag == width || anti == width) return 1;
        if (row[r] == -width || col[c] == -width || diag == -width || anti == -width) return 2;
        return 0;
    }
};

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe obj = new TicTacToe(n);
 * int param_1 = obj.move(row,col,player);
 */
 