class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int res = 0;
        for (int i = 0; i < nums.size(); ++i) {
            string num_str = to_string(nums[i]);
            if (num_str.size() % 2 == 0)
                ++res;
        }
        return res;
    }
};
