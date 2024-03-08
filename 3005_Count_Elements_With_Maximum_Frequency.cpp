class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        unordered_map<int, int> counter;
        int maximum = 0, res = 0;
        for (int num : nums) {
            counter[num]++;
            if (counter[num] > maximum) {
                maximum = counter[num];
                res = 0;
            }
            if (counter[num] == maximum) res += counter[num];
        }

        return res;
    }
};
