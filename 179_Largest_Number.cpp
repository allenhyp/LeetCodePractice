class Solution {
private:
    static bool compare(string a, string b) {
        return a + b > b + a;
    }
public:
    string largestNumber(vector<int>& nums) {
        vector<string> numstr;
        string res = "";
        for (int num : nums) numstr.push_back(to_string(num));
        sort(numstr.begin(), numstr.end(), compare);
        for (string s : numstr) res += s;
        return res[0] == '0' ? "0" : res;
    }
};
