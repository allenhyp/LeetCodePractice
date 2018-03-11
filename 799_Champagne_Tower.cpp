#include <iostream>
#include <vector>
using namespace std;

class Solution {
private:
    double got_wine(int r, int c, vector<vector<double>> &result) {
        if (c < 0 || c > r)
            return 0;
        if (result[r][c] != -2)
            return result[r][c];
        double left, right;
        left = got_wine(r - 1, c - 1, result) - 1;
        if (left < 0) left = 0;
        right = got_wine(r - 1, c, result) - 1;
        if (right < 0) right = 0;
        result[r][c] = (left + right) / 2;
        return result[r][c];
    }
public:
    double champagneTower(int poured, int query_row, int query_glass) {
        vector<vector<double>>result(100, vector<double>(100, -2));
        result[0][0] = double(poured);
        got_wine(query_row, query_glass, result);
        return min(result[query_row][query_glass], 1.0);
    }
};

int main(void) {
    Solution my_solution;
    cout << my_solution.champagneTower(18,6,2) << endl;
    return 0;
}
