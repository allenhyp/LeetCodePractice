class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<bool> dp (s.size() + 1, false);
        dp[0] = true;
        for (int i = 0; i < s.size(); ++i) {
            for (string word : wordDict) {
                int n = word.size();
                if ((i - n >= -1 && dp[i - n + 1]) && s.substr(i - n + 1, n) == word) {
                    dp[i + 1] = true;
                }
            }
        }
        return dp[s.size()];
    }
};
