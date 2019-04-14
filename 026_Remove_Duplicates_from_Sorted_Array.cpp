class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        if (n < 2) return n;
        int i = 1;
        for (int j = 1; j < n; ++j) {
            if (nums[j] != nums[i - 1])
                nums[i++] = nums[j];
        }
        return i;
    }
};
