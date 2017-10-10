class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        for (int i = 1; i < n; i++) {
            triangle[i][0] += triangle[i-1][0];
            for (int j = 1; j < i; j++)
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j]);
            triangle[i][i] += triangle[i-1][i-1];            
        }
        int minPath = INT_MAX;
        for (int i = 0; i < n; i++) {
            minPath = min(triangle[n-1][i], minPath);
        }
        return minPath;
    }
};
