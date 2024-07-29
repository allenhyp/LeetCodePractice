class Solution {
public:
    int minReorder(int n, vector<vector<int>>& connections) {
        unordered_map<int, vector<int>> out, in;
        int ans = 0;
        for (auto connection : connections) {
            int from = connection[0], to = connection[1];
            out[from].push_back(to);
            in[to].push_back(from);
        }

        queue<int> q;
        q.push(0);
        vector<int> visited (n, false);
        while (!q.empty()) {
            int cur = q.front(); q.pop();
            visited[cur] = true;
            for (int to : out[cur]) {
                if (!visited[to]) {
                    ans++;
                    q.push(to);
                }
            }

            for (int from : in[cur]) {
                if (!visited[from]) q.push(from);
            }
        }
        return ans;
    }
};
