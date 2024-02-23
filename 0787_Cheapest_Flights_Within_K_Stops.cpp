class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        unordered_map<int, vector<pair<int, int>>> adj;
        for (auto flight : flights) {
            adj[flight[0]].push_back({flight[1], flight[2]});
        }
        vector<int> costs (n, INT_MAX);
        costs[src] = 0;
        queue<pair<int, pair<int, int>>> q; // (stops, node, cost)
        q.push({-1, {src, 0}});
        while (!q.empty()) {
            auto it = q.front(); q.pop();
            int stops = it.first;
            int node = it.second.first;
            int cost = it.second.second;
            if (stops == k) continue;
            for (auto next : adj[node]) {
                if (costs[next.first] > cost + next.second) {
                    costs[next.first] = cost + next.second;
                    q.push({stops+1, {next.first, costs[next.first]}});
                }
            }
        }
        return costs[dst] == INT_MAX ? -1 : costs[dst];
    }
};
