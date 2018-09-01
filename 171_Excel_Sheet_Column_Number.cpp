class Solution {
public:
    int titleToNumber(string s) {
        int size = s.size(), result = 0;
        for (int i = 0; i < size; i++) {
            result = result * 26 + s[i] - '@';
        }
        return result;
    }
};
