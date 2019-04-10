class Solution {
private:
    vector<pair<int, int>> directions = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        if (rooms.size() == 0 || rooms[0].size() == 0) return;
        int m = rooms.size(), n = rooms[0].size();
        queue<pair<int, int>> q;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (rooms[i][j] == 0)
                    q.push({i, j});
            }
        }
        while (!q.empty()) {
            int i = q.front().first, j = q.front().second;
            q.pop();
            for (auto dir : directions) {
                int di = i + dir.first, dj = j + dir.second;
                if (0 <= di && di < m && 0 <= dj && dj < n 
                    && rooms[di][dj] == INT_MAX) {
                    rooms[di][dj] = rooms[i][j] + 1;
                    q.push({di, dj});
                }
            }
        }
    }
};
