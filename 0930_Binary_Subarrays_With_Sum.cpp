class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        int res = 0, cur = 0, l = 0, count = 0;
        for (int r = 0; r < nums.size(); r++) {
            cur += nums[r];
            if (nums[r] == 1) count = 0;
            while (l <= r && cur >= goal) {
                if (cur == goal) count++;
                cur -= nums[l++];
            }
            res += count;
        }
        return res;
    }
};
