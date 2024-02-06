class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> dic;
        vector<vector<string>> res;
        for (string word : strs) {
            string occ = word;
            sort(occ.begin(), occ.end());
            dic[occ].push_back(word);
        }
        for (auto group : dic) res.push_back(group.second);
        return res;
    }
};
