class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph (numCourses, vector<int> ());
        vector<int> indegree (numCourses, 0);
        queue<int> q;
        vector<int> res;
        
        for (auto pre : prerequisites) {
            graph[pre[1]].push_back(pre[0]);
            ++indegree[pre[0]];
        }

        for (int i = 0; i < numCourses; ++i) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }

        while (!q.empty()) {
            int target = q.front(); q.pop();
            res.push_back(target);
            for (auto adj : graph[target]) {
                if (--indegree[adj] == 0) {
                    q.push(adj);
                }
            }
        }

        return res.size() == numCourses ? res : vector<int> ();
    }
};
