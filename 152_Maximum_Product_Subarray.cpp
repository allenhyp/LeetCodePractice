class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int m = nums[0], max_here = nums[0], min_here = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            int temp = max_here;
            max_here = max(max(max_here * nums[i], min_here * nums[i]), nums[i]);
            min_here = min(min(temp * nums[i], min_here * nums[i]), nums[i]);
            m = max(m, max_here);
        }
        return m;
    }
};