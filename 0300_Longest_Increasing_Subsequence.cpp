// Dynamic programming
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int size = nums.size();
        if (size < 2) return size;
        int maximum = 0;
        vector<int> dp (size, 1);
        for (int i = 1; i < size; ++i) {
            for (int j = 0; j < i; ++j) {
                if (nums[i] > nums[j]) {
                    dp[i] = max(dp[j] + 1, dp[i]);
                }
            }
        }
        
        for (int i = 0; i < size; ++i) {
            maximum = max(maximum, dp[i]);
        }
        return maximum;
    }
};


// Binary search substitution for first number greater than the one searching to greedily find the best sequence
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> sub ({nums[0]});
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > sub.back())
                sub.push_back(nums[i]);
            else 
                sub[lower_bound(sub.begin(), sub.end(), nums[i]) - sub.begin()] = nums[i];
        }
        return sub.size();
    }
};
