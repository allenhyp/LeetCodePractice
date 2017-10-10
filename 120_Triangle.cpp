class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        vector<int> dp(n, 0);
        dp[0] = triangle[0][0];
        int pre, cur;
        for (int i = 1; i < n; i++) {
            pre = dp[0];
            dp[0] += triangle[i][0];
            for (int j = 1; j <= i; j++) {
                if (j == i) dp[j] = pre + triangle[i][j];
                else {
                    cur = pre;
                    pre = dp[j];
                    dp[j] = min(cur, dp[j]) + triangle[i][j];
                }
            }
        }
        int minPath = INT_MAX;
        for (int i = 0; i < n; i++) {
            minPath = min(dp[i], minPath);
        }
        return minPath;
    }
};
