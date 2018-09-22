class Solution {
private:
    int worker(vector<int>& nums, int offset) {
        int n = nums.size() - (offset == 0 ? 1 : 0);
        if (n == 0) return 0;
        else if (n == 1) return nums[0];
        int pre = 0, cur = 0;
        for (int i = offset; i < n; i++) {
            int temp = pre;
            pre = cur;
            cur = max(temp + nums[i], pre);
        }
        return cur;
    }
public:
    int rob(vector<int>& nums) {
        return max(worker(nums, 0), worker(nums, 1));
    }
};
