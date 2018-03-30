class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        unordered_map<int, int> edges;
        int size = wall.size(), min_bricks = size;
        for (int i = 0; i < size; i++) {
            for (int j = 0, width = 0; j < wall[i].size() - 1; j++) {
                min_bricks = min(min_bricks, size - (++edges[width += wall[i][j]]));
            }
        }
        return min_bricks;
    }
};
