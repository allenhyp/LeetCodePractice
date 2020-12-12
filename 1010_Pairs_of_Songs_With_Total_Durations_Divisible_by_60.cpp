class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        int res = 0;
        vector<int> remainders (60, 0);
        for (int t : time) {
            int r = t % 60;
            int need = r > 0 ? 60 - r : 0;
            res += remainders[need];
            ++remainders[r];
        }
        return res;
    }
};
