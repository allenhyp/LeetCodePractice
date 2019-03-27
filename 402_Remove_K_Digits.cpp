class Solution {
public:
    string removeKdigits(string num, int k) {
        stack<char> stk;
        int count = k;
        for (char c : num) {
            while (!stk.empty() && stk.top() > c && count > 0) {
                stk.pop();
                --count;
            }
            stk.push(c);
        }
        string ans;
        while (!stk.empty()) {
            ans = stk.top() + ans;
            stk.pop();
        }
        int cursor = 0, keep = num.length() - k;
        while (cursor < keep && ans[cursor] == '0') cursor++;
        return cursor == keep ? "0" : ans.substr(cursor, keep - cursor);
    }
};
