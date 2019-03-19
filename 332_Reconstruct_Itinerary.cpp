class Solution {
private:
    unordered_map<string, multiset<string>> targets;
    vector<string> path;
    void dfs(string departure) {
        while (targets[departure].size()) {
            string arrival = *targets[departure].begin();
            targets[departure].erase(targets[departure].begin());
            dfs(arrival);
        }
        path.push_back(departure);
    }
public:
    vector<string> findItinerary(vector<pair<string, string>> tickets) {
        for (auto t : tickets) targets[t.first].insert(t.second);
        dfs("JFK");
        return vector<string> (path.rbegin(), path.rend());
    }
};
