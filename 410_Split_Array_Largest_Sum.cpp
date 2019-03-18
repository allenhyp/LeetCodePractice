class Solution {
public:
    int splitArray(vector<int>& nums, int m) {
        long long left = LLONG_MIN, right = 0;
        for (int num : nums) {
            if (num > left) left = num;
            right += num;
        }
        while (left < right) {
            long long mid = (left + right) / 2, cur = 0;
            int need = 1;
            for (int num : nums) {
                if (cur + num > mid) {
                    ++need;
                    cur = 0;
                }
                cur += num;
            }
            if (need > m) left = mid + 1;
            else right = mid;
        }
        return left;
    }
};
