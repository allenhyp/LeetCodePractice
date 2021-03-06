class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> visited ({{0, -1}});
        int sum = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (k != 0) sum = (sum + nums[i]) % k;
            else sum += nums[i];
            if (visited.find(sum) != visited.end()) {
                if (i - visited[sum] > 1)
                    return true;
            }
            else visited[sum] = i;
        }
        return false;
    }
};
