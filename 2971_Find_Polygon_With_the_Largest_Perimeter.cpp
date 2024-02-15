class Solution {
public:
    long long largestPerimeter(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        long long postfix = 0;
        for (auto num : nums) postfix += num;
        for (int i = nums.size() - 1; i >= 2; i--) {
            if (postfix - nums[i] <= nums[i]) {
                postfix -= nums[i];
            } else {
                return postfix;
            }
        }
        return -1;
    }
};
