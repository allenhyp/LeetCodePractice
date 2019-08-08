class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> dic;
        dic[0]++;
        int res = 0, cur = 0;
        for (int num : nums) {
            cur += num;
            res += dic[cur - k];
            dic[cur]++;
        }
        return res;
    }
};
