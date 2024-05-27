class Solution {
public:
    string largestPalindromic(string num) {
        vector<int> counter (10);
        string ans = "";
        int single = -1;

        for (int i = 0; i < num.size(); i++) counter[num[i] - '0']++;
        for (int i = 9; i >= 0; i--) {
            if (ans.empty() && i == 0) break;
            while (counter[i] > 1) {
                ans.push_back(i + '0');
                counter[i] -= 2;
            }
            if (counter[i] == 1 && single == -1) single = i;
        }
        string tail = string(ans.rbegin(), ans.rend());
        if (ans.empty() && single == -1) return "0";
        if (single != -1) ans.push_back(single + '0');
        ans += tail;
        return ans;
    }
};