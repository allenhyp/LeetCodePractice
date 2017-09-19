class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        if (m < 1) return false;
        int n = matrix[0].size();
        if (n < 1) return false;
        int i = 0, j = n - 1;
        while (i < m && j >= 0) {
            if (matrix[i][j] > target) j--;
            else if (matrix[i][j] < target) i++;
            else return true;
        }
        return false;
    }
};

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        if (m < 1) return false;
        int n = matrix[0].size();
        if (n < 1) return false;
        int i = 0;
        while (i < m && target >= matrix[i][0]) {
            int lower = 0, upper = n;
            while (lower < upper) {
                int mid = (lower + upper) / 2;
                if (matrix[i][mid] > target) upper = mid;
                else if (matrix[i][mid] < target) lower = mid + 1;
                else return true;
            }
            i++;
        }
        return false;
    }
};
