class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> subs;
        vector<int> sub;
        generate_subset(nums, 0, sub, subs);
        return subs;
    }
    void generate_subset(vector<int>& nums, int start, vector<int>& sub, vector<vector<int>>& subs) {
        subs.push_back(sub);
        for (int i = start; i < nums.size(); i++) {
            sub.push_back(nums[i]);
            generate_subset(nums, i + 1, sub, subs);
            sub.pop_back();
        }
    }
};
