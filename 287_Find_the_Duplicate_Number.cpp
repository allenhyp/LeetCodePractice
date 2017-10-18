class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        if (nums.size() < 2) return -1;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 1; i++) {
            if (nums[i] == nums[i+1]) return nums[i];
        }
    }
};

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        if (nums.size() < 2) return -1;
        int slow = nums[0];
        int fast = nums[nums[0]];
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[nums[fast]];
        }
        int target = 0;
        while (target != slow) {
            slow = nums[slow];
            target = nums[target];
        }
        return target;
    }
};
