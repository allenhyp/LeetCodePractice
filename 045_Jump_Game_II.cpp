// Greedy (O(n))
class Solution {
public:
    int jump(vector<int>& nums) {
        int result = 0;
        int last = 0;
        int cur = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (i > last) {
                last = cur;
                result++;
            }
            cur = max(cur, i + nums[i]);
        }
        return result;
    }
};

// Dynamic programing (O(n^2) exceed time limit)
class Solution {
public:
    int jump(vector<int>& nums) {
        int size = nums.size();
        vector<int> steps = {0};
        for (int i = 1; i < size; i++) {
            steps.push_back(INT_MAX);
        }
        for (int i = 0; i < size; i++) {
            for (int j = 1; j <= nums[i]; j++) {
                if (i + j < size) {
                    if (steps[i] + 1 < steps[i + j]) {
                        steps[i + j] = steps[i] + 1;
                    }
                }
            }
        }
        return steps.back();
    }
};
