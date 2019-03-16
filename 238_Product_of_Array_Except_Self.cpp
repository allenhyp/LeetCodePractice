class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        int front = 1, back = 1;
        vector<int> res (n, 1);
        for (int i = 0; i < n; ++i) {
            res[i] *= front;
            front *= nums[i];
            res[n - i - 1] *= back;
            back *= nums[n - i - 1];
        }
        return res;
    }
};
