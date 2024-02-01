class Solution {
public:
    vector<vector<int>> divideArray(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res (1, vector<int>());
        int j = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (res[j].size() == 3) {
                res.push_back({nums[i]});
                j++;
            }
            else if (res[j].size() == 0 || nums[i] - res[j][0] <= k) {
                res[j].push_back(nums[i]);                
            } else {
                return {};
            }   
        }
        return res;
    }
};
