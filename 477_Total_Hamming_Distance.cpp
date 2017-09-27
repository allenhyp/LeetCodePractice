class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        int size = nums.size();
        int *zeroOrOne = new int[2];
        int result = 0;
        while (true) {
            int zeroCount = 0;
            zeroOrOne[0] = 0;
            zeroOrOne[1] = 0;
            for (int i = 0; i < size; i++) {
                if (nums[i] == 0) zeroCount++;
                zeroOrOne[nums[i] % 2]++;
                nums[i] = nums[i] >> 1;
            }
            result += zeroOrOne[0] * zeroOrOne[1];
            if (zeroCount == size) return result;
        }
    }
};
