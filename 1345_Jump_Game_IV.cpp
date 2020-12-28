class Solution {
public:
    int minJumps(vector<int>& arr) {
        int n = arr.size();
        unordered_map<int, vector<int>> graph;
        vector<bool> visited (n, false);
        queue<int> q;
        int steps = 0;
        for (int i = 0; i < n; ++i)
            graph[arr[i]].push_back(i);
        
        visited[0] = true;
        q.push(0);
        while (!q.empty()) {
            for (int i = q.size(); i > 0; --i){
                int t = q.front();
                q.pop();
                if (t == n - 1) return steps;
                vector<int>& next = graph[arr[t]];
                next.push_back(t - 1);
                next.push_back(t + 1);
                for (auto j : next) {
                    if (j >= 0 && j < n && !visited[j]) {
                        visited[j] = true;
                        q.push(j);
                    }
                }
                next.clear();
            }
            steps++;
        }
        
        return 0;
    }
};
