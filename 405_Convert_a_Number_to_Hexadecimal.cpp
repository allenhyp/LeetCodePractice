class Solution {
    const string HEX = "0123456789abcdef";
public:
    string toHex(int num) {
        string result = "";
        if (num == 0) return "0";
        int count = 0;
        while (num && count++ < 8) {
            result = HEX[num & 0xf] + result;
            num >>= 4;
        }
        return result;
    }
};
