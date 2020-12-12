class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() < 3) return nums.size();
        bool flag = false;
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] == nums[i - 1]) {
                if (flag) nums.erase(nums.begin() + i--);
                else flag = true;
            }
            else flag = false;
        }
        return nums.size();
    }
};
