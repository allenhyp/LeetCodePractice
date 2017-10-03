class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int size = nums.size();
        vector<vector<int> > result;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < size - 2; i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue;
            int lower = i + 1, upper = size - 1;
            while (lower < upper) {
                int sum = nums[i] + nums[lower] + nums[upper];
                if (sum < 0) lower++;
                else if (sum > 0) upper--;
                else {
                    vector<int> row = {nums[i], nums[lower], nums[upper]};
                    result.push_back(row);
                    while (lower < upper && nums[lower] == row[1]) lower++;
                    while (lower < upper && nums[upper] == row[2]) upper--;
                }
            }
        }
        return result;
    }
};
