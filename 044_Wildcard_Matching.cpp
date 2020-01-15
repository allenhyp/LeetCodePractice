class Solution {
public:
    bool isMatch(string s, string p) {
        int i = 0, j = 0, star = -1, match = 0;
        while (i < s.size()) {
            // advance both iterator for both string and pattern
            if (j < p.size() && (s[i] == p[j] || p[j] == '?')) {
                ++i;
                ++j;
            }
            // advance only pattern
            else if (j < p.size() && p[j] == '*') {
                star = j++;
                match = i;
            }
            // advance only string
            else if (star > -1) {
                j = star + 1;
                i = ++match;
            }
            else return false;
        }
        for (; p[j] == '*'; ++j);
        return j == p.size();
    }
};
