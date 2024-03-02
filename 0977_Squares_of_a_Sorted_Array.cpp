class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> res (nums.size());
        int l = 0, r = nums.size()-1;
        int i = nums.size() - 1;
        while (l <= r) {
            if (abs(nums[l]) > abs(nums[r]))
                res[i--] = (int) pow(nums[l++], 2);
            else
                res[i--] = (int) pow(nums[r--], 2);
        }
        return res;
    }
};
