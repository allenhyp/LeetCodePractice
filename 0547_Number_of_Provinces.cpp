class Solution {
private:
    bool dfs(vector<vector<int>>& isConnected, vector<bool>& visited, int index) {
        if (visited[index]) return false;
        visited[index] = true;
        for (int j = 0; j < isConnected[index].size(); ++j) {
            if (isConnected[index][j]) dfs(isConnected, visited, j);
        }
        return true;
    }
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        int count = 0;
        vector<bool> visited (n, false);
        for (int i = 0; i < n; ++i) {
            if (dfs(isConnected, visited, i)) count++;
        }
        return count;
    }
};
