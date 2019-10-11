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


class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> res;
        for (int num : nums) {
            auto it = lower_bound(res.begin(), res.end(), num);
            if (it == res.end()) res.push_back(num);
            else *it = num;
        }
        
        return res.size();
    }
};
