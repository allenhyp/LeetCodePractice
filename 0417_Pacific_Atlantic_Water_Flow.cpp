class Solution {
private:
    const vector<int> dr = { 0, 1, 0, -1 };
    const vector<int> dc = { -1, 0, 1, 0 };
    vector<vector<int>> visited;
    vector<vector<int>> ans;
    void dfs(vector<vector<int>>& heights, int r, int c, int pre_height, int des) {
        if (r < 0 || r >= heights.size() || c < 0 || c >= heights[0].size()
            || heights[r][c] < pre_height || (visited[r][c] & des) == des) return;
        visited[r][c] |= des;
        if (visited[r][c] == 3) ans.push_back({r, c});
        for (int i = 0; i < 4; i++) {
            dfs(heights, r+dr[i], c+dc[i], heights[r][c], visited[r][c]);
        }
    }
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int m = heights.size(), n = heights[0].size();
        visited.resize(m, vector<int> (n, 0));

        for (int r = 0; r < m; r++) {
            dfs(heights, r, 0, INT_MIN, 1);
            dfs(heights, r, n-1, INT_MIN, 2);
        }
        for (int c = 0; c < n; c++) {
            dfs(heights, 0, c, INT_MIN, 1);
            dfs(heights, m-1, c, INT_MIN, 2);
        }

        return ans;
    }
};
