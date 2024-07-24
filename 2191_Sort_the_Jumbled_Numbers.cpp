class Solution {
public:
    vector<int> sortJumbled(vector<int>& mapping, vector<int>& nums) {
        vector<pair<int,int>> remapped;
        for (int i = 0; i < nums.size(); ++i) {
            string num_str = to_string(nums[i]);
            for (int j = 0; j < num_str.size(); ++j)
                num_str[j] = '0' + mapping[num_str[j] - '0'];
            remapped.push_back({stoi(num_str), i});
        }
        sort(remapped.begin(), remapped.end());
        vector<int> ret;
        for (auto r : remapped) {
            ret.push_back(nums[r.second]);
        }
        return ret;
    }
};
