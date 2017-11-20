class Solution {
public:
    int longestPalindrome(string s) {
        map<char, int> d;
        for (int i = 0; i < s.size(); i++) {
            d[s[i]]++;
        }
        int result = 0;
        bool odd = true;
        for (int i = 0; i < d.size(); i++) {
            if (d[i] % 2 == 1) {
                result += d[i] - 1;
                if (odd) {
                    result++;
                    odd = false;
                }
            }
            else {
                result += d[i];
            }
        }
        return result;
    }
};
