class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int n = nums.size(), sum = 0, left = 0, min_len = INT_MAX;
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            while (sum >= s) {
                min_len = min(min_len, i - left + 1);
                sum -= nums[left++];
            }
        }
        return min_len == INT_MAX ? 0 : min_len;
    }
};
