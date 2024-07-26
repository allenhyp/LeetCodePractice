class Solution {
public:
    int findTheCity(int n, vector<vector<int>>& edges, int distanceThreshold) {
        // Floyd-Warshall
        vector<vector<int>> dist (n, vector<int> (n, INT_MAX));
        for (vector<int> edge : edges) {
            dist[edge[0]][edge[1]] = edge[2];
            dist[edge[1]][edge[0]] = edge[2];
        }
        for (int k = 0; k < n; ++k) {
            dist[k][k] = 0;
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    if (dist[i][k] == INT_MAX || dist[j][k] == INT_MAX)
                        continue;
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }

        int minimal_adjs = n, ans = -1;
        for (int i = 0; i < n; ++i) {
            int adjs = 0;
            for (int j = 0; j < n; ++j) {
                if (dist[i][j] <= distanceThreshold) adjs++;
            }
            if (adjs <= minimal_adjs) {
                minimal_adjs = adjs;
                ans = max(ans, i);
            }
        }

        return ans;
    }
};
