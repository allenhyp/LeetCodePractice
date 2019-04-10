class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        if (matrix.size() == 0 || matrix[0].size() == 0)
            return matrix;
        int m = matrix.size(), n = matrix[0].size();
        int maximum = m + n;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (matrix[i][j] > 0) {
                    int up = i > 0 ? matrix[i - 1][j] : maximum;
                    int left = j > 0 ? matrix[i][j - 1] : maximum;
                    matrix[i][j] = min(up, left) + 1;
                }
            }
        }
        for (int i = m - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                if (matrix[i][j] > 0) {
                    int down = i < m - 1 ? matrix[i + 1][j] : maximum;
                    int right = j < n - 1 ? matrix[i][j + 1] : maximum;
                    matrix[i][j] = min(min(down, right) + 1, matrix[i][j]);
                }
            }
        }
        return matrix;
    }
};
