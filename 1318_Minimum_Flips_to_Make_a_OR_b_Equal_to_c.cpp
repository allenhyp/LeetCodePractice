class Solution {
public:
    int minFlips(int a, int b, int c) {
        int ba, bb, bc, res = 0;
        while (a | b | c) {
            ba = a & 1;
            bb = b & 1;
            bc = c & 1;
            res += abs(ba + bb - bc);
            if (ba & bb & bc == 1) --res;
            a >>= 1;
            b >>= 1;
            c >>= 1;
        }
        return res;
    }
};
