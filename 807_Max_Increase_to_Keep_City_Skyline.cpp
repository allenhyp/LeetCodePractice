class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        vector<int> r;
        vector<int> c;
        int h = 0, result = 0;
        for (int i = 0; i < grid.size(); i++) {
            h = 0;
            for (int j = 0; j < grid[i].size(); j++) {
                h = max(h, grid[i][j]);
            }
            r.push_back(h);
        }
        for (int j = 0; j < grid[0].size(); j++) {
            h = 0;
            for (int i = 0; i < grid.size(); i++) {
                h = max(h, grid[i][j]);
            }
            c.push_back(h);
        }
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[i].size(); j++) {
                result += min(r[i], c[j]) - grid[i][j];
            }
        }
        return result;
    }
};
