class Solution {
public:
    string shortestPalindrome(string s) {
        string rev = s;
        reverse(rev.begin(), rev.end());
        string temp = s + "#" + rev;
        vector<int> table(temp.size(), 0);
        for (int i = 1; i < table.size(); i++) {
            int j = table[i - 1];
            while (j > 0 && temp[i] != temp[j]) {
                j = table[j - 1];
            }
            table[i] = (j += temp[i] == temp[j]);
        }
        return rev.substr(0, s.size() - table[temp.size() - 1]) + s;
    }
};
