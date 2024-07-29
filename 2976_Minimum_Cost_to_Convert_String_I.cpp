class Solution {
private:
    const int CHAR_COUNT = 26;

    vector<vector<int>> buildConversionGraph(vector<char>& original, vector<char>& changed, vector<int>& cost) {
        // Initialization
        vector<vector<int>> graph (CHAR_COUNT, vector<int> (CHAR_COUNT, INT_MAX));
        for (int i = 0; i < CHAR_COUNT; ++i) graph[i][i] = 0;
        for (int i = 0; i < original.size(); ++i) {
            int from = original[i] - 'a';
            int to = changed[i] - 'a';
            int cst = cost[i];
            graph[from][to] = min(graph[from][to], cst);
        }

        // Floyd-Warshall
        for (int k = 0; k < CHAR_COUNT; ++k) {
            for (int i = 0; i < CHAR_COUNT; ++i) {
                for (int j = 0; j < CHAR_COUNT; ++j) {
                    if (graph[i][k] == INT_MAX || graph[k][j] == INT_MAX) continue;
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);
                }
            }
        }
        return graph;
    }

public:
    long long minimumCost(string source, string target, vector<char>& original, vector<char>& changed, vector<int>& cost) {
        vector<vector<int>> graph = buildConversionGraph(original, changed, cost);
        long long ret = 0;
        for (int i = 0; i < source.size(); ++i) {
            int s = source[i] - 'a';
            int t = target[i] - 'a';
            if (graph[s][t] == INT_MAX) return -1;
            ret += graph[s][t];
        }
        return ret;
    }
};
