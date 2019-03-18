class Solution {
private:
    vector<long> dept;
    int dfs(vector<long>& dept, int s) {
        while (s < dept.size() && !dept[s]) s++;
        int res = INT_MAX;
        long prev = 0;
        for (int i = s + 1; i < dept.size(); ++i) {
            if (dept[i] != prev && dept[s] * dept[i] < 0) {
                dept[i] += dept[s];
                res = min(res, 1 + dfs(dept, s + 1));
                prev = dept[i] -= dept[s];
            }
        }
        return res == INT_MAX ? 0 : res;
    }
public:
    int minTransfers(vector<vector<int>>& transactions) {
        vector<long> dept;
        unordered_map<int, long> balance;
        for (auto t : transactions) {
            balance[t[0]] -= t[2];
            balance[t[1]] += t[2];
        }
        for (auto b : balance) {
            if (b.second != 0) dept.push_back(b.second);
        }
        return dfs(dept, 0);
    }
};
