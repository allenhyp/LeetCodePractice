class Solution {
public:
    int rob(vector<int>& nums) {
        int a = 0, b = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (i % 2 == 0)
                a = max(a + nums[i], b);
            else
                b = max(b + nums[i], a);
        }
        return max(a, b);
    }
};


class Solution {
public:
    int rob(vector<int>& nums) {
        int a = 0, b = 0, temp;
        for (int i = 0; i < nums.size(); i++) {
            temp = a > b ? a : b;
            a = b + nums[i];
            b = temp;
        }
        return  a > b ? a : b;
    }
};
