class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        vector<int> dp (30, 0);
        int n = days.size();
        for (int i = 1, j = 0; i <= 366; ++i) {
            if (j >= n) {
                return dp[(i - 1) % 30];
            }
            else if (i != days[j]) {
                dp[i % 30] = dp[(i - 1) % 30];
            }
            else {
                int min_cost = dp[(i - 1) % 30] + costs[0];
                min_cost = min(min_cost, dp[max((i - 7), 0) % 30] + costs[1]);
                min_cost = min(min_cost, dp[max((i - 30), 0) % 30] + costs[2]);
                dp[i % 30] = min_cost;
                j++;
            }
        }
        return dp[6];
    }
};
