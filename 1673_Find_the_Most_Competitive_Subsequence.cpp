class Solution {
public:
    vector<int> mostCompetitive(vector<int>& nums, int k) {
        vector<int> stack;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            while (!stack.empty() && nums[i] < stack.back() && k - stack.size() + 1 <= n - i)
                stack.pop_back();
            if (stack.size() < k) stack.push_back(nums[i]);
        }
        return stack;
    }
};
