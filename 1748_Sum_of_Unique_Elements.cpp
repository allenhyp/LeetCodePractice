class Solution {
public:
    int sumOfUnique(vector<int>& nums) {
        unordered_map<int, int> dic;
        for (int num : nums) {
            if (dic.find(num) == dic.end()) dic[num] = 1;
            else dic[num] += 1;
        }
        
        int sum = 0;
        for (auto p : dic) {
            if (p.second == 1) sum += p.first;
        }
        
        return sum;
    }
};
