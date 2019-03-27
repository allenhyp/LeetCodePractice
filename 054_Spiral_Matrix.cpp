class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if (matrix.empty()) return {};
        int m = matrix.size(), n = matrix[0].size();
        int l = 0, r = n - 1, t = 0, b = m - 1, i = 0;
        vector<int> res (m * n);
        while (l <= r && t <= b) {
            for (int col = l; col <= r; ++col) res[i++] = matrix[t][col];
            if (++t > b) break;
            for (int row = t; row <= b; ++row) res[i++] = matrix[row][r];
            if (--r < l) break;
            for (int col = r; col >= l; --col) res[i++] = matrix[b][col];
            if (--b < t) break;
            for (int row = b; row >= t; --row) res[i++] = matrix[row][l];
            if (++l > r) break;
        }
        return res;
    }
};
