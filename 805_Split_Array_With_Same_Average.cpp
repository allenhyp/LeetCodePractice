class Solution {
public:
    bool combinationSum(vector<int>& nums, int idx, int k, int target) {
        if (k == 0) return target == 0;
        for (int i = idx; i <= nums.size() - k && target >= nums[i] * k; i++) {
            if (nums[i] <= target && combinationSum(nums, i + 1, k - 1, target - nums[i]))
                return true;
        }
        return false;
    }

    bool splitArraySameAverage(vector<int>& A) {
        int n = A.size(), m = n / 2, total = accumulate(A.begin(), A.end(), 0);
        sort(A.begin(), A.end());
        for (int i = 1; i <= m; i++) {
            if (total * i % n == 0 && combinationSum(A, 0, i, total * i / n))
                return true;
        }
        return false;
    }
};
