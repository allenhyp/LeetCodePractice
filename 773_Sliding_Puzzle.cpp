#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <stack>
#include <set>
using namespace std;

class Solution {
    private:
        unordered_map<int, vector<int>> moves{{0,{1,3}},{1,{0,2,4}},{2,{1,5}},{3,{0,4}},{4,{3,5,1}},{5,{4,2}}};
    public:
        int slidingPuzzle(vector<vector<int>>& board) {
            string s = to_string(board[0][0]) + to_string(board[0][1]) + to_string(board[0][2]) 
                        + to_string(board[1][0]) + to_string(board[1][1]) + to_string(board[1][2]);
            int steps = 0;
            unordered_set<string> m;
            stack<pair<string, int>> st_1({{s, s.find('0')}}), st_2;
            while (!st_1.empty() && st_1.top().first != "123450") {
                for (auto new_zero : moves[st_1.top().second]) {
                    auto str = st_1.top().first;
                    swap(str[st_1.top().second], str[new_zero]);
                    if (m.insert(str).second)
                        st_2.push({str, new_zero});
                }
                st_1.pop();
                if (st_1.empty()) {
                    steps++;
                    swap(st_1, st_2);
                }
            }
            return st_1.empty() ? -1 : steps;
        }
};


class Solution {
    unordered_map<int, vector<int>> moves{{0,{1,3}},{1,{0,2,4}},{2,{1,5}},{3,{0,4}},{4,{3,5,1}},{5,{4,2}}};
    public:
        void dfs(string s, unordered_map<string, int> m, int cur_zero, int swap_zero, int cur_move, int& min_moves) {
            swap(s[cur_zero], s[swap_zero]);
            if (s == "123450") min_moves = min(min_moves, cur_move);
            if (cur_move < min_moves && (m[s] == 0 || m[s] > cur_move)) {
                m[s] = cur_move;
                for (auto new_zero : moves[swap_zero]) dfs(s, m, swap_zero, new_zero, cur_move + 1, min_moves);
            }
        }
        int slidingPuzzle(vector<vector<int>>& board) {
            int min_moves = INT_MAX;
            string s = to_string(board[0][0]) + to_string(board[0][1]) + to_string(board[0][2]) 
                + to_string(board[1][0]) + to_string(board[1][1]) + to_string(board[1][2]);
            dfs(s, unordered_map<string, int>() = {}, s.find('0'), s.find('0'), 0, min_moves);
            return min_moves == INT_MAX ? -1 : min_moves;
        }
};


/*
class Solution {
private:
    vector<vector<int> > correctBoard{{1, 2, 3}, {4, 5, 0}};
public:
    int slidingPuzzle(vector<vector<int>>& board) {
        int steps = 0;
        int i = 0, j = 0;
        int up, down, left, right;
        printBoard(board);
        for (; i < 2; i++) {
            for(; j <= 3; j++) {
                if (board[i][j] == 0){
                    break;
                }
            }
            if (board[i][j] == 0)
                break;
            j = 0;
        }
        int d;
        cin >> d;
        while (!isCorrect(board)) {
            if (i == 1) {
                up = distanceToCorrect(board[i - 1][j], i, j);
                down = INT_MAX;                
            }
            else {
                down = distanceToCorrect(board[i + 1][j], i, j);
                up = INT_MAX;
            }
            left = j > 0 ? distanceToCorrect(board[i][j - 1], i, j) : INT_MAX;
            right = j < 2 ? distanceToCorrect(board[i][j + 1], i, j) : INT_MAX;
            cout << up << ',' << down << ',' << left << ',' << right << endl;
            cin >> d;
            int minima = minimumCandidate(up, down, left, right);
            switch (minima) {
                case 0:
                    board[i][j] = board[i - 1][j];
                    board[i - 1][j] = 0;
                    i = 0;
                    break;
                case 1:
                    board[i][j] = board[i + 1][j];
                    board[i + 1][j] = 0;
                    i = 1;
                    break;
                case 2:
                    board[i][j] = board[i][j - 1];
                    board[i][j - 1] = 0;
                    j = j - 1;
                    break;
                case 3:
                    board[i][j] = board[i][j + 1];
                    board[i][j + 1] = 0;
                    j = j + 1;
                    break;
            }
            printBoard(board);
        }
        return steps;
    }

    int distanceToCorrect(int t, int r, int c) {
        cout << "what?\n";
        cout << t << ',' << r << ',' << c << endl;
        switch (t) {
            case 2:
                c -= 1;
                break;
            case 3:
                c -= 2;
                break;
            case 4:
                r -= 1;
                break;
            case 5:
                r -= 1;
                c -= 1;
                break;
            default:
                break;
        }
        return r*r + c*c;
    }

    int minimumCandidate(int u, int d, int l, int r) {
        int minima = min(u, min(d, min(l, r)));
        if (minima == u) return 0;
        else if (minima == d) return 1;
        else if (minima == l) return 2;
        else return 3;
    }

    void printBoard(vector<vector<int> >& b) {
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 3; j++) {
                cout << b[i][j] << ", ";
            }
            cout << endl;
        }
    }

    bool isCorrect(vector<vector<int> >& b) {
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 3; j++) {
                if (b[i][j] != correctBoard[i][j]) return false;
            }
        }
        return true;
    }
};
*/

int main(void) {
    vector<vector<int> > b = {{1,2,3},{5,4,0}};
    Solution mySolution;
    cout << mySolution.slidingPuzzle(b) << endl;
    return 0;
}
