class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph (numCourses, vector<int> ());
        vector<int> indegree (numCourses, 0);
        vector<bool> visited (numCourses, false);
        queue<int> q;
        
        for (auto pre : prerequisites) {
            graph[pre[1]].push_back(pre[0]);
            ++indegree[pre[0]];
        }

        for (int i = 0; i < numCourses; ++i) {
            if (indegree[i] == 0) {
                visited[i] = true;
                q.push(i);
            }
        }

        while (!q.empty()) {
            int target = q.front(); q.pop();
            for (auto adj : graph[target]) {
                if (!visited[adj] && --indegree[adj] == 0){
                    q.push(adj);
                    visited[adj] = true;
                }
            }
        }

        for (auto v : visited) {
            if (!v) return false;
        }
        return true;
    }
};
