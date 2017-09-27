class Solution {
public:
    int hammingDistance(int x, int y) {
        int z = x ^ y;
        int result = 0;
        for (; z != 0; z >>= 1) {
            if (z & 1) result++;
        }
        return result;
    }
};
