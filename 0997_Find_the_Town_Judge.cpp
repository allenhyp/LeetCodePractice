class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        vector<int> in_bounds (n, 0);
        for (int i = 0; i < trust.size(); i++) {
            int a = trust[i][0], b = trust[i][1];
            in_bounds[b-1]++;
            in_bounds[a-1]--;
        }
        for (int i = 0; i < n; i++) {
            if (in_bounds[i] == n-1) return i+1;
        }
        return -1;
    }
};
