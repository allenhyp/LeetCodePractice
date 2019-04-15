class Solution {
private:
    int m, n;
    void dfs(vector<vector<char>>& grid, int i, int j) {
        if (i >= 0 && i < m && j >= 0 && j < n && grid[i][j] > '0') {
            grid[i][j] = '0';
            dfs(grid, i - 1, j);
            dfs(grid, i, j - 1);
            dfs(grid, i + 1, j);
            dfs(grid, i, j + 1);
        }
    }
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.size() == 0 || grid[0].size() == 0) return 0;
        m = grid.size(), n = grid[0].size();
        int res = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] > '0') {
                    res++;
                    dfs(grid, i, j);
                }
            }
        }
        return res;
    }
};
