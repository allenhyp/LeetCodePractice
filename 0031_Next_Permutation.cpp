class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int low_index = nums.size();
        for (int i = nums.size() - 2; i >= 0; --i) {
            if (nums[i] < nums[i+1]) {
                low_index = i;
                break;
            }
        }

        if (low_index == nums.size()) {
            sort(nums.begin(), nums.end());
            return;
        }

        int next_larger_index = low_index + 1;
        for (int i = nums.size() - 1; i > low_index + 1; --i) {
            if (nums[i] < nums[next_larger_index] && nums[i] > nums[low_index]) {
                next_larger_index = i;
            }
        }

        swap(nums[low_index], nums[next_larger_index]);
        sort(nums.begin()+low_index+1, nums.end());
        return;
    }
};
