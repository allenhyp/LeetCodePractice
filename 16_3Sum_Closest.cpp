class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int result;
        int size = nums.size();
        int minDet = INT_MAX;
        for (int i = 0; i < size - 2; i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue;
            int lo = i + 1, hi = size - 1;
            while (lo < hi) {
                int sum = nums[i] + nums[lo] + nums[hi];
                int det = target > sum ? target - sum : sum - target;
                if (det < minDet) {
                    result = sum;
                    minDet = det;
                }
                if (sum < target) lo++;
                if (sum > target) hi--;
                if (sum == target) return sum;
            }
        }
        return result;
    }
};
