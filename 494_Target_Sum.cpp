class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        // sum(P) - sum(N) = S
        // sum(P) + sum(N) + sum(P) - sum(N) = S + sum(P) + sum(N)
        // 2 * sum(P) = S + sum
        // target:sum(P) = (S + sum) / 2
        
        int sum = 0;
        for (int num : nums) sum += num;
        if (S > sum || (S + sum) % 2 != 0) return 0;
        int target = (S + sum) / 2;
        vector<int> dp (target + 1, 0);
        dp[0] = 1;
        for (int num : nums) {
            for (int i = target; i >= num; --i) {
                dp[i] += dp[i - num];
            }
        }
        return dp[target];
    }
};
