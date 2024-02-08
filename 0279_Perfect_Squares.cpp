class Solution {
public:
    int numSquares(int n) {
        vector<int> dp (n + 1, INT_MAX);
        dp[0] = 0;
        dp[1] = 1;
        for (int i = 1; i <= n; ++i) {
            for (int s = 1; s * s <= i; ++s) {
                dp[i] = min(dp[i], dp[i - s * s] + 1);
            }
        }
        return dp[n];
    }
};
