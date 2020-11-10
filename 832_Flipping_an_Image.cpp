class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
        int m = A.size(), n = A[0].size();
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n / 2; ++j) {
                int tmp = A[i][j];
                A[i][j] = -A[i][n - j - 1] + 1;
                A[i][n - j - 1] = - tmp + 1;
            }
            if (n % 2 == 1) A[i][n / 2] = -A[i][n / 2] + 1;
        }
        
        return A;
    }
};