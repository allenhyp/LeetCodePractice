class Solution {
private:
    int size;
    void permute(vector<int> nums, int start, vector<vector<int>>& result) {
        if (start == size - 1) {
            result.push_back(nums);
            return;
        }
        for (int i = start; i < size; i++) {
            if (i != start && nums[i] == nums[start]) continue;
            swap(nums[i], nums[start]);
            permute(nums, start + 1, result);
            // swap(nums[l], nums[i]);
        }
    }
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        size = nums.size();
        vector<vector<int>> result;
        permute(nums, 0, result);
        return result;
    }
};
