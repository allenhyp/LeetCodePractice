class Solution {
public:
    int minimumLength(string s) {
        int l = 0, r = s.size()-1;
        while (l < r && s[l] == s[r]) {
            char t = s[l];
            while (l <= r && s[l] == t) ++l;
            while (l <= r && s[r] == t) --r;
        }
        return r - l + 1;
    }
};
