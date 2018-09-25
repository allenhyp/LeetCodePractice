class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = nums.size(), i = 0, j, k;
        while (i < n) {
            j = i;
            while (nums[j] == 0 && j < n)
                j++;
            for (k = 0; k < j - i && j + k < n; k++) {
                nums[i + k] = nums[j + k];
                nums[j + k] = 0;
            }
            i++;
            // i = i == j ? i + 1 : j;
        }
        return;
    }
};
