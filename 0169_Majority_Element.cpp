class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int counter = 1, major = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            if (counter == 0) major = nums[i];
            counter += nums[i] == major ? 1 : -1;
        }
        return major;
    }
};


class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size();
        if (nums.size() < 1) return 0;
        return majority(nums, 0, n - 1);
    }
private:
    int majority(vector<int>& nums, int left, int right) {
        if (left == right) return nums[left];
        int mid = (left + right) / 2;
        int ml = majority(nums, left, mid);
        int mr = majority(nums, mid + 1, right);
        if (ml == mr) return ml;
        return count(nums.begin() + left, nums.begin() + right + 1, ml) > 
            count(nums.begin() + left, nums.begin() + right + 1, mr) ?
            ml : mr;
    }
};
