class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int count = 0;
        int maximum = 0;
        unordered_map<int, int> table ({{0, 0}});
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) count--;
            else count++;
            if (table.find(count) != table.end())
                maximum = max(maximum, i - table[count]+1);
            else
                table[count] = i+1;
        }
        return maximum;
    }
};
