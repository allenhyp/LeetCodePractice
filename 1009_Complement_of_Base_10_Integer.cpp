class Solution {
public:
    int bitwiseComplement(int N) {
        int ans = N == 0 ? 1 : 0, ref = 1;
        while (N > 0) {
            ans += ref * (N & 1 ? 0 : 1);
            ref <<= 1;
            N >>= 1;
        }
        return ans;
    }
};
