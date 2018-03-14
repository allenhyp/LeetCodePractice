class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n < 2) return 0;
        vector<int> former(n, 0);
        vector<int> later(n, 0);
        for (int i = 1, valley = prices[0]; i < n; i++) {
            valley = min(valley, prices[i]);
            former[i] = max(former[i - 1], prices[i] - valley);
        }
        for (int i = n - 2, peak = prices[n - 1]; i > 0; i--) {
            peak = max(peak, prices[i]);
            later[i] = max(later[i + 1], peak - prices[i]);
        }
        int max_profit = 0;
        for (int i = 0; i < n; i++) {
            max_profit = max(max_profit, former[i] + later[i]);
        }
        return max_profit;
    }
};
