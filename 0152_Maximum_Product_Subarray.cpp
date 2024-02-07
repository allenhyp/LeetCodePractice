class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];
        int res = nums[0];
        int max_prod = res, min_prod = res;
        for (int i = 1; i < nums.size(); i++) {
            int num = nums[i];
            if (num < 0) swap(max_prod, min_prod);
            max_prod = max(num, max_prod * num);
            min_prod = min(num, min_prod * num);
            res = max(res, max_prod);
        }
        return res;
    }
};
