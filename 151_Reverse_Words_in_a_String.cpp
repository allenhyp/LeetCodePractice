class Solution {
public:
    string reverseWords(string s) {
        istringstream is(s);
        string tmp;
        is >> s;
        if (s[0] == ' ') s = "";
        while (is >> tmp) s = tmp + " " + s;
        return s;
    }
};
