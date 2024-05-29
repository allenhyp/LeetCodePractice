class Solution {
private:
    int dfs(int cur_id, vector<int>& debts) {
        while (cur_id < debts.size() && debts[cur_id] == 0) cur_id++;
        if (cur_id == debts.size()) return 0;
        int min_transactions = INT_MAX;
        for (int next_id = cur_id + 1; next_id < debts.size(); next_id++) {
            if (debts[cur_id] * debts[next_id] < 0) {
                debts[next_id] += debts[cur_id];
                min_transactions = min(min_transactions, dfs(cur_id + 1, debts) + 1);
                debts[next_id] -= debts[cur_id];
            } 
        }

        return min_transactions;
    }
public:
    int minTransfers(vector<vector<int>>& transactions) {
        unordered_map<int, int> debts_map;
        int max_id = 0;
        for (auto transaction : transactions) {
            int giver = transaction[0];
            int taker = transaction[1];
            int amount = transaction[2];
            if (debts_map.find(giver) == debts_map.end()) debts_map[giver] = 0;
            debts_map[giver] += amount;
            if (debts_map.find(taker) == debts_map.end()) debts_map[taker] = 0;
            debts_map[taker] -= amount;
            max_id = max(max_id, max(giver, taker));
        }

        vector<int> debts (max_id + 1, 0);
        for (auto d = debts_map.begin(); d != debts_map.end(); d++) {
            debts[d->first] = d->second;
        }
        
        return dfs(0, debts);
    }
};
